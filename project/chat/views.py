from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserChatRequest, Chat
import openai
import os
import environ
from pathlib import Path
from gtts import gTTS
from io import BytesIO
from datetime import date
from django.db.models import F
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
User = get_user_model()

class ChatGPTAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self, request):
        user = request.user
        today = date.today()
        chat_request_count = UserChatRequest.objects.filter(user=user, date=today).first()
        if chat_request_count is None:
            chat_request_count = UserChatRequest(user=user, request_count=0, date=today)
            chat_request_count.save()
        
        limit = user.daily_chat_limit

        user_chats = Chat.objects.filter(user=request.user).order_by('created_at')
        conversations = [{'role': chat.role, 'content': chat.content} for chat in user_chats]

        return Response({'conversations': conversations, 'count': chat_request_count.request_count, 'limit': limit}, status=status.HTTP_200_OK)

    def post(self, request):
        today = date.today()
        user_chat_request, _ = UserChatRequest.objects.get_or_create(
            user=request.user,
            date=today
        )
        

        limit = request.user.daily_chat_limit
        if user_chat_request.request_count >= limit:
            return Response({'error': 'You have exceeded the chat request limit for today.'}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        
        UserChatRequest.objects.filter(pk=user_chat_request.pk).update(request_count=F('request_count') + 1)

        # 요청으로부터 받은 데이터 추출
        user_input = request.data.get('user_input')
        interview_topic = request.data.get('interview_topic')
        chats = Chat.objects.filter(user=request.user).order_by('created_at')

        # 기존 채팅 내역과 새로운 채팅을 합침
        combined_chats = [{"role": chat.role, "content": chat.content} for chat in chats]

        # 시스템 시작 메시지 추가 (기존 채팅 내역이 없을 경우)
        if not user_input and not chats:
            system_start_message = {
                "role": "system", 
                "content": f"I want you to act as an {interview_topic} interviewer. I will be the candidate and you will ask me the interview questions for the position position. I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me the questions and wait for my answers. Do not write explanations. Ask me the questions one by one like an interviewer does and wait for my answers. My first sentence is Hi'. Response with English"
            }
            combined_chats.append(system_start_message)

            # 시스템 저장
            ai_chat = Chat(user=request.user, role=system_start_message['role'], content=system_start_message['content'])
            ai_chat.save()

        # 사용자 입력을 채팅 내역에 저장
        if user_input:
            user_chat = {"role": "user", "content": user_input}
            combined_chats.append(user_chat)

            # 사용자 입력을 데이터베이스에 저장
            user_input_chat = Chat(user=request.user, role="user", content=user_input)
            user_input_chat.save()

        # 새로운 채팅 내역을 OpenAI API에 요청 보내기
        openai.api_key = env('OPENAI_API_KEY')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=combined_chats,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        ai_response = response['choices'][0]['message']['content']

        # AI 응답을 채팅 내역에 저장
        ai_chat = Chat(user=request.user, role="assistant", content=ai_response)
        ai_chat.save()

        # TTS 생성
        tts = gTTS(text=ai_response, lang='en', slow=False)
        audio_bytes_io = BytesIO()
        tts.write_to_fp(audio_bytes_io)
        audio_bytes_io.seek(0)

        authenticated_user = request.user

        user_identifier = authenticated_user.username
        audio_file = f"{user_identifier}_ai_response.mp3"
        audio_file_path = os.path.join(BASE_DIR, "staticfiles", "tts", audio_file)

        with open(audio_file_path, "wb") as f:
            f.write(audio_bytes_io.read())

        base_address = request.build_absolute_uri("/")[:-1]
        audio_url = f"{base_address}/staticfiles/tts/{audio_file}"

        # 응답값 프론트엔드로 전달
        return Response({'response': ai_response, 'audio_url': audio_url}, status=status.HTTP_200_OK)
