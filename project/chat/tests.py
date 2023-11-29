from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Chat, UserChatRequest
from datetime import date

class ChatGPTAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)

        self.url = reverse('chat-gpt')
    '''
    테스트 케이스 시작 전 필요한 설정을 위한 setUp 메서드
    테스트 클라이언트 인스턴스 생성
    테스트를 위한 사용자 생성 및 인증
    테스트할 URL 설정
    '''

    def test_get_chat_history(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('conversations', response.data)

    '''
    GET 요청을 통한 채팅 기록 조회 테스트
    GET 요청을 보내고 응답을 받음
    응답 상태 코드와 응답 데이터 확인

    '''

    def test_post_chat_request(self):
        data = {'user_input': 'Hello', 'interview_topic': 'Software Engineering'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('response', response.data)

    '''
    POST 요청 데이터 설정
    요청을 보내고 응답을 받음
    응답 상태 코드와 응답 데이터 확인
    '''   

    def test_request_limit_exceeded(self):
        UserChatRequest.objects.create(user=self.user, request_count=5, date=date.today())
        data = {'user_input': 'Hi again'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    '''
    사용자 채팅 요청 제한 초과 시 테스트
    사용자 채팅 요청 수 초과 상황을 위한 레코드 생성
    POST 요청 데이터 설정
    POST 요청을 보내고 응답을 받음
    응답 상태 코드 확인 (429 Too Many Requests)
    '''
