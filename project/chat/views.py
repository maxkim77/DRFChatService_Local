#Chat/views.py
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
from datetime import date
from django.db.models import F
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

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

        # 사용자의 채팅 요청 수 확인
        chat_request_count = UserChatRequest.objects.filter(user=user, date=today).first()
        if chat_request_count is None:
            # 새 요청 수 객체 생성 및 저장
            chat_request_count = UserChatRequest(user=user, request_count=0, date=today)
            chat_request_count.save()

        # 사용자의 일일 채팅 제한 가져오기
        limit = user.daily_chat_limit

        # 사용자의 채팅 기록 가져오기
        user_chats = Chat.objects.filter(user=request.user).order_by('created_at')
        conversations = [{'role': chat.role, 'content': chat.content} for chat in user_chats]

        # 채팅 내역 및 요청 수 반환
        return Response({'conversations': conversations, 'count': chat_request_count.request_count, 'limit': limit}, status=status.HTTP_200_OK)

    def post(self, request):
        today = date.today()
        # 사용자의 채팅 요청 객체 가져오기 또는 생성
        user_chat_request, _ = UserChatRequest.objects.get_or_create(user=request.user, date=today)

        # 일일 채팅 제한 확인
        limit = request.user.daily_chat_limit
        if user_chat_request.request_count >= limit:
            # 제한 초과 시 에러 반환
            return Response({'error': 'You have exceeded the chat request limit for today.'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        # 요청 수 증가 및 저장
        UserChatRequest.objects.filter(pk=user_chat_request.pk).update(request_count=F('request_count') + 1)

        # 요청 데이터 추출
        user_input = request.data.get('user_input')
        interview_topic = request.data.get('interview_topic')
        chats = Chat.objects.filter(user=request.user).order_by('created_at')

        # 기존 및 새 채팅 내역 결합
        combined_chats = [{"role": chat.role, "content": chat.content} for chat in chats]

        # 시스템 시작 메시지 추가 (채팅 내역이 없을 경우)
        if not user_input and not chats:
            system_start_message = {
                "role": "system", 
                "content": "시작 메시지 내용"
            }
            combined_chats.append(system_start_message)

            # 시스템 메시지 저장
            ai_chat = Chat(user=request.user, role=system_start_message['role'], content=system_start_message['content'])
            ai_chat.save()

        # 사용자 입력 저장
        if user_input:
            user_chat = {"role": "user", "content": user_input}
            combined_chats.append(user_chat)

            # 사용자 입력 데이터베이스에 저장
            user_input_chat = Chat(user=request.user, role="user", content=user_input)
            user_input_chat.save()

        # OpenAI API에 채팅 내역 요청
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

        # AI 응답 저장
        ai_chat = Chat(user=request.user, role="assistant", content=ai_response)
        ai_chat.save()

        # AI 응답 반환
        return Response({'response': ai_response}, status=status.HTTP_200_OK)
