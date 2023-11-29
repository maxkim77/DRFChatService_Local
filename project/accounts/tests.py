from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

class SignupTestCase(APITestCase):
    def test_signup(self):
        data = {
            'email': 'test@example.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
        }
        response = self.client.post(reverse('rest_register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')

    def test_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'somepassword',
        }
        response = self.client.post(reverse('logout')) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')
        self.client.login(email='test@example.com', password='somepassword')

    def test_logout(self):
        response = self.client.post(reverse('rest_logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MyPageTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')
        self.client.login(email='test@example.com', password='somepassword')  

    def test_mypage(self):
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')
    
class MyPageTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')
        response = self.client.post(reverse('dj_rest_auth:login'), {'email': 'test@example.com', 'password': 'somepassword'})
        self.token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_mypage(self):
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    """
    회원가입 기능에 대한 테스트 케이스
    - test_signup: 새 사용자를 생성하는 POST 요청을 보내고, HTTP 201 Created 상태 코드로 응답하는지 확인
    
    로그인 기능에 대한 테스트 케이스
    - setUp: 테스트를 위해 새 사용자 생성
    - test_login: 생성된 사용자로 로그인하는 POST 요청을 보내고, HTTP 200 OK 상태 코드로 응답하는지 확인
    
    로그아웃 기능에 대한 테스트 케이스
    - setUp: 테스트를 위해 새 사용자 생성 및 로그인 후 토큰 획득
    - test_logout: 획득한 토큰을 사용해 로그아웃하는 POST 요청을 보내고, HTTP 200 OK 상태 코드로 응답하는지 확인
    
    마이페이지 기능에 대한 테스트 케이스
    - setUp: 테스트를 위해 새 사용자 생성 및 로그인 후 토큰 획득, 테스트 클라이언트에 인증 토큰 설정
    - test_mypage: 마이페이지 정보 조회 GET 요청을 보내고, HTTP 200 OK 상태 코드와 사용자 이메일 정보를 응답하는지 확인
    """
