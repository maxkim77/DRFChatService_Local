# DRFChatService

## 0. Chat Service 개요


- 사용자가 영어 회화 및 인터뷰를 연습할 수 있는 플랫폼

- 해외 취업을 생각 하거나 영어 스피킹 실력을 기르고 싶은 사람을 위한 플랫폼


## 1. 목표와 기능
### 1.1 목표

- 프론트 프로젝트 확장 기능: OpenAI의 GPT-3.5 모델을 이용한 챗봇 애플리케이션 개발

  
- API 기능: 기존 OpenAI에서 제공하는 API 대신 직접 구축한 서버(DRF:Dangro Rest Framework)를 통해 요청

  
- AI 통합 기능 : HTML/CSS 프로젝트에 AI 댓글 및 답변 기능 통합


- 프론트와 백앤드 분리 : JS를 활용한 백앤드 통신

  
### 1.2 기능
- DRF 활용: 모든 구현은 Django Rest Framework를 사용하여 진행


- 사용자 인증: JWT를 활용한 회원가입 및 로그인 기능 구현


- 챗봇 API: Django 서버 내 ChatGPT API 구현


- 사용 제한: 각 사용자는 하루에 최대 5번 요청 가능


- 데이터베이스 관리: 채팅 내역 저장 및 조회 기능



## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- FE:


![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=javascript&logoColor=black)

- BE:


![Python](https://img.shields.io/badge/Python-3.8-3776AB.svg)
![Django](https://img.shields.io/badge/Django-3.x-092E20.svg)


- Deployment:

  
![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange?style=flat&logo=amazonaws)
![Gunicorn](https://img.shields.io/badge/gunicorn-%2023.0-green.svg)
![Nginx](https://img.shields.io/badge/nginx-1.21.3-blue.svg?style=flat&logo=nginx&logoColor=white)


### 2.2 배포 URL
https://www.studyin.co.kr/


## 3. 요구사항 명세와 기능 명세
![0](https://github.com/maxkim77/DRFChatService/assets/141907655/650c9dd6-d2e2-491a-8f7e-f56b5815c874)
### 3.1 기본 요구사항
- DRF 활용: 모든 구현은 Django Rest Framework를 사용하여 진행


- 사용자 인증: 회원가입 및 로그인 기능 구현


- 챗봇 API: Django 서버 내 ChatGPT API 구현


- 사용 제한: 각 사용자는 하루에 최대 5번 요청 가능


- 데이터베이스 관리: 채팅 내역 저장 및 조회 기능


### 3.2 선택 요구사항
- 도메인 및 배포: 개인 도메인 등록 및 HTTPS 적용


- OAuth2 연동: 카카오, GitHub 등 OAuth2 연결


## 4. 개발 일정 및 프로젝트구조 / 플로우 차트
### 4.1 개발일정(WBS)


![Untitled diagram-2023-11-21-043933](https://github.com/maxkim77/DRFChatService/assets/141907655/f8895ba5-8142-49d9-a08f-e3f95b6ff341)


| Scope              | WBS Level | WBS ID | WBS Element Title      | Completion  |
|--------------------|-----------|--------|------------------------|-------------|
| Planning           | 1         | plan1  | WBS, Model, Requirements|  |
| Planning           | 1         | plan2  | ERD                    |   |
| Design             | 2         | des1   | Screen Design          |   |
| Design             | 2         | des2   | URL Design             |   |
| Development        | 3         | dev1   | Page Implementation    |   |
| Development        | 3         | dev2   | CRUD Implementation    |   |
| Development        | 3         | dev3   | User Registration & Login |  |
| Development        | 3         | dev4   | Unique User Permissions |  |
| Development        | 3         | dev5   | ChatGPT Integration    |  |
| UI/UX              | 4         | ui1    | UI Implementation      |  |
| Deployment         | 5         | dep1   | Deployment             |  |
| Final Preparations | 6         | prep1  | Readme Completion      |  |
| Final Preparations | 6         | prep2  | Presentation Preparation|  |
| Presentation       | 7         | pres1  | Final Presentation     |  |

### 4.2 프로젝트 구조


### 4.3 플로우 차트
![제목 없는 다이어그램 drawio](https://github.com/maxkim77/DRFChatService/assets/141907655/f4b4ebc5-e11d-4a51-ab4f-67155312c625)

### 4.4 URL 기획
| 엔드포인트          | HTTP 메서드 | 기능                            | 앱          |
|----------------------|-------------|---------------------------------|-------------|
| `/admin/`            | GET         | 관리자 패널 접속                 | admin       |
| `/accounts/join/`    | POST        | 사용자 등록                     | accounts    |
| `/accounts/mypage/`  | GET         | 내 정보 페이지 조회              | accounts    |
| `/accounts/token/`    | POST        | JWT 토큰 획득                   | accounts    |
| `/accounts/token/refresh/` | POST | JWT 토큰 갱신                   | accounts    |
| `/chatbot/chats/`    | GET         | 모든 채팅 목록 조회             | chatbot     |
| `/chatbot/chats/`    | POST        | 채팅 생성                       | chatbot     |
| `/chatbot/chats/{id}/` | GET      | 특정 채팅 조회                   | chatbot     |
| `/chatbot/chats/{id}/` | PUT      | 특정 채팅 수정                   | chatbot     |
| `/chatbot/chats/{id}/` | DELETE   | 특정 채팅 삭제                   | chatbot     |



### 4.5 설치 라이브러리
```
aiohttp==3.8.5
aiosignal==1.3.1
asgiref==3.7.2
async-timeout==4.0.2
attrs==23.1.0
certifi==2023.7.22
charset-normalizer==3.2.0
click==8.1.6
Django==4.2.3
django-cors-headers==4.2.0
django-environ==0.10.0
djangorestframework==3.14.0
frozenlist==1.4.0
gTTS==2.3.2
idna==3.4
multidict==6.0.4
openai==0.27.8
pytz==2023.3
requests==2.31.0
sqlparse==0.4.4
tqdm==4.65.0
urllib3==2.0.4
yarl==1.9.2
djangorestframework-simplejwt==4.6
Djoser==2.1
django-allauth==0.49.0  # Adjust the version as needed
dj-rest-auth==2.2.5  # Adjust the version as needed
```


## 5. 역할 분담: 김정원 Back-End Developer


## 6. 와이어프레임 / UI
![1](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/d128d630-e9d2-4076-a28a-cb413e3d22a9)
![2](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/190b0ea7-37d3-46a5-93f7-d7ed391b77ed)

## 7. 데이터베이스 모델링:


![Untitled (1)](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/08e230ca-6fa1-4fc0-a460-766f54af200a)

## 8. 아키텍처: 시스템 아키텍처 설계
## 9. 메인 기능: 주요 기능 및 작동 방식
- 주요 페이지 구현

  
![10](https://github.com/maxkim77/DRFChatService/assets/141907655/c1e5f843-451c-45a8-b179-9ae48b437d19)


- Signup 기능

  
![3](https://github.com/maxkim77/DRFChatService/assets/141907655/d40ff50c-ac3b-4142-b5eb-0a4307a15776)

  
- Login 기능


![1](https://github.com/maxkim77/DRFChatService/assets/141907655/b71ca5a5-da7b-4bad-b71a-a0c3f87c5a6a)


- Logout 기능


![4](https://github.com/maxkim77/DRFChatService/assets/141907655/ea879056-399d-468b-b547-9dcbefd73c71)


- Chat Gpt - DRF 연결


https://github.com/maxkim77/DRFChatService/assets/141907655/0bcc53bf-03ce-4ede-84f6-b13ddd8a12c2


- 로그인을 한 유저만 사용가능


![1](https://github.com/maxkim77/DRFChatService/assets/141907655/4692f2f4-351a-4ca3-ab58-b8128ad12bc2)


- 각 유저당 5번 요청 제한

![ezgif com-resize](https://github.com/maxkim77/DRFChatService/assets/141907655/71e00498-098a-4871-918c-d5daa8637d54)


- 채팅내역 데이터베이스 저장 재로그인후 조회 가능


![ezgif com-resize (1)](https://github.com/maxkim77/DRFChatService/assets/141907655/976f44c7-4f42-4b21-ae66-8a51aa77d507)


## 📜10. 에러 및 해결: 개발 중 발생한 주요 문제 및 해결 방법
**⚒ 오류 1: "400 (Bad Request)" 오류 발생**

  - **원인:** 프론트엔드와 백엔드 간의 데이터 불일치

  - **해결책:**

    - **프론트엔드 수정:**
    
        필수 필드와 데이터 형식 확인 후 전송
        ```javascript
        fetch('http://127.0.0.1:8000/api/user/register/', {
          method: 'POST',
          mode: 'cors', 
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: username,
            email: email,
            password: password,
            password2: confirmPassword
          })
        })
        ```
    
    - **오류 메시지 처리:** 프론트엔드에서 오류 메시지 처리

    - **서버 로그 정상작동 확인:**

**⚒ 오류 2: AssertionError in Allauth**
   - 사용자 인증, 등록, 로그인, 비밀번호 기능등 제대로 동작 하지 않을 때 발생하는 에러 네임

  - **원인:** ACCOUNT_USERNAME_REQUIRED 설정이 False로 되어 있음

  - **해결책:** `settings.py`에서 `ACCOUNT_USERNAME_REQUIRED`를 True로 설정

**⚒ 오류 3: 토큰 저장 및 사용 오류**
  - 일반 token 인증 구현시 발생한 오류
  - **해결책:**

    - **클라이언트 코드 수정:**
    
        토큰 키 일치 확인
        ```javascript
        localStorage.setItem('token', data.Token);
        ```

    - **API 호출 시 토큰 포함:**
    
        Authorization 헤더에 토큰 추가
        ```javascript
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
        }
        ```


 **⚒ 오류 4: UNIQUE constraint failed: authtoken_token.user_id**
  - 일반 token 구현시 발생한 오류
  - **해결책:**

  
     이미 생성된 토큰을 반환하고 기존 토큰 삭제 후 새 토큰 생성

 **💡 알게된 점:**

  - 토큰 관련 오류 해결 방법 및 토큰 관리 방식의 차이(JWT vs. Token Authentication)를 알게됨.

- **Jwt Authentication in Views**

  - **설정:** `rest_framework_simplejwt.authentication.JWTAuthentication`을 `authentication_classes`에 추가

  - **사용 예시:**
  ```python
  from rest_framework_simplejwt.authentication import JWTAuthentication
  from rest_framework.permissions import IsAuthenticated
  from rest_framework.views import APIView

  class ExampleView(APIView):
      authentication_classes = [JWTAuthentication]
      permission_classes = [IsAuthenticated]

      def get(self, request):
          # 인증된 사용자의 정보는 `request.user`를 통해 접근
          pass

- **Token Authentication in Views**

- **설정**: rest_framework.authentication.TokenAuthentication을 authentication_classes에 추가

- **사용 예시**:

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 인증된 사용자의 정보는 request.user를 통해 접근
        pass
```

##  📖11. 개발하며 느낀점: 프로젝트를 통해 얻은 경험 및 느낀 점
- DRF책을 집필하면서 개념만 공부를 했는데, 실제로 적용해보니 단순해보이면서도 매우 어렵게 느낌
- 특히 일반토큰을 통해 구현을 마쳤지만, JWT토큰도 한번 도전해봐야겠다는 생각에 WBS 계획보다 기간을 늘려 6번의 프로젝트 재생성을 끝에 통신에 성공함
- 백엔드 개발자로 공부를 하고 있지만, 프론트개발자와 소통하거나 오류를 해결하려면 Js 지식도 갖춰야 함을 느낌 추가적으로 Vanilla Js 말고도 React 등 다양한 공부를 해야겠다는 생각이 듬
- DRF를 하며 어려웠던 점: 생각보다 참고할 만한 강의나 영상이 적었던 점.  찾아보면 블로그 글이 있긴한데 에러 상황이 달라 적용할 수 없었던점. 영어로 된 강의나 문서가 많았던 점. DRF는 GPT의 할루시네이션이 조금 심했던 점
- 하지만 어려운 만큼 DRF는 희소성 있고 경쟁력 있는 기술이라는 생각이 듬
- 서버 배포를 하며 어려웠던 점: 마찬가지로 관련 한국어 강의 등이 적어 적용하기 어려웠음. 글만 보고 이해하기 부족하다는 느낌이 듬.
- 실제 백엔드 배포를 AWSlightsail Ubuntu, Gunicorn, Nginx 등을 통해 해보니 서버관련 각 스택들에 대해 개략적인 느낌을 익힐 수 있었음
  
##  👦12. 백엔드 개발자 : 김정원 Back-End Developer

