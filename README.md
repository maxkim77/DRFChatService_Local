# ☘ DRF와 Chat Gpt로 만든 영어인터뷰 서비스 - English Max
![제목 없는 디자인](https://github.com/maxkim77/DRFChatService/assets/141907655/7e90ccc0-12dd-4aeb-878b-fb1347cb54b6)

## 📌 0. Chat Service 개요


- 사용자가 영어 회화 및 인터뷰를 연습할 수 있는 플랫폼

- 영어 인터뷰 준비가 있거나 영어 스피킹 실력을 기르고 싶은 사람을 위한 플랫폼


##  ✨1. 목표와 기능
### 1.1 목표
- DRF 활용 웹 개발: 모든 구현은 Django Rest Framework를 사용하여 진행

 
- API 기능 구현: 기존 OpenAI에서 제공하는 API 대신 직접 구축한 서버(DRF:Dangro Rest Framework)를 통해 요청


- 프론트와 백앤드 분리 : JS를 통해 HTTP/HTTPS 백엔드 서버 통신

  
### 1.2 기능


- 사용자 인증: JWT를 활용한 회원가입 및 로그인 기능 구현


- 챗봇 API: Django 서버 내 ChatGPT API 구현


- 사용 제한: 각 사용자는 하루에 최대 5번 요청 가능


- 데이터베이스 관리: 채팅 내역 저장 및 조회 기능



##  🎉2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- FE:


  ![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
  ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)


✔ Tailwind 사용으로 css 간결화


- BE:


  ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
  ![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)



- Deployment:


  [![GitHub](https://img.shields.io/badge/GitHub-100000.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
  [![AWS Lightsail](https://img.shields.io/badge/AWS-Lightsail-FF9900.svg?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/lightsail/)
  [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420.svg?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
  [![Gunicorn](https://img.shields.io/badge/Gunicorn-green.svg?style=for-the-badge&logo=gunicorn)](https://gunicorn.org/)
  [![Nginx](https://img.shields.io/badge/Nginx-blue.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
  [![DB SQLite](https://img.shields.io/badge/DB-SQLite-003B57.svg?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)

✔ Githug 프론트 배포, AWS Lightsail 백엔드 배포
### 2.2 배포 및 관련 URL: https://dev.maxworld7070.net/
📍Backend 배포용 : https://github.com/maxkim77/DRFChatService_BE
📍Frontend 배포용 : https://github.com/maxkim77/DRFChatService_FE

##  🎊3. 요구사항 명세와 기능 명세
- Tool : Mindmeister

[![MindMeister](https://img.shields.io/badge/MindMeister-Link-blue.svg)](https://www.mindmeister.com/)

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


##  🗓4. 개발 일정 및 프로젝트구조 / 플로우 차트
### 4.1 개발일정(WBS)

- Tool : Mermaid

  [![Mermaid](https://img.shields.io/badge/Mermaid-Link-blue.svg)](https://mermaid.js.org/)

![Untitled diagram-2023-11-21-043933](https://github.com/maxkim77/DRFChatService/assets/141907655/f8895ba5-8142-49d9-a08f-e3f95b6ff341)


| Scope              | WBS Level | WBS ID | WBS Element Title      | Completion (Completed Date)  |
|--------------------|-----------|--------|------------------------|-------------|
| Planning           | 1         | plan1  | WBS, Model, Requirements| ✅ 11.21. |
| Planning           | 1         | plan2  | ERD                    |  ✅ 11.21. |
| Design             | 2         | des1   | Screen Design          |  ✅ 11.21. |
| Design             | 2         | des2   | URL Design             |  ✅ 11.21. |
| Development        | 3         | dev1   | Page Implementation    |  ✅ 11.22. |
| Development        | 3         | dev2   | CRUD Implementation    |  ✅ 11.22. |
| Development        | 3         | dev3   | User Registration & Login | ✅ 11.25.  |
| Development        | 3         | dev4   | Unique User Permissions | ✅ 11.26 |
| Development        | 3         | dev5   | ChatGPT Integration    | ✅ 11.27. |
| UI/UX              | 4         | ui1    | UI Implementation      |  ✅ 11.27. |
| Deployment         | 5         | dep1   | Deployment             | ✅ 11.28. |
| Final Preparations | 6         | prep1  | Readme Completion      | ✅ 11.29. |
| Final Preparations | 6         | prep2  | Presentation Preparation| ✅ 11.30. |
| Presentation       | 7         | pres1  | Final Presentation     | ✅11.31. |

### 4.2 프로젝트 구조
```
📦project
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂chat
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂project
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.env
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂staticfiles
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┗ 📜requirements.txt
📦env
📦FE
 ┣ 📂css
 ┣ 📂js
 ┣ 📂Repo
 ┗ 📜index.html
```

### 4.3 플로우 차트
- Tool : draw.io


  [![draw.io](https://img.shields.io/badge/draw.io-Link-blue.svg)](https://app.diagrams.net/)


![제목 없는 다이어그램 drawio (1)](https://github.com/maxkim77/DRFChatService/assets/141907655/f4cf2b3c-a783-4fd8-a3c4-ecfbe079e7c7)

### 4.4 URL 기획
| 엔드포인트                    | HTTP 메서드 | 기능                          | 앱           | 비고                    |
|-------------------------------|-------------|-------------------------------|--------------|-------------------------|
| /admin/                       |  -           | 관리자 패널 접속               | admin        |                         |
| /account/join/                | POST        | 사용자 등록                   | accounts     |                         |
| /account/login/               | POST        | 로그인                        | accounts     |                         |
| /account/logout/              | POST        | 로그아웃                      | accounts     |                         |
| /account/mypage/             | GET         | 내정보조회                     | accounts     |* 로그인후 mypage로 리다이렉트 될 때<br> HTTP 응답 200 성공여부 테스트 용 url  |
| /api/chat/gpt/               | POST         | GPT 챗봇 API                  | chat         |                         |
| /account/token/               | POST        | JWT 토큰 획득                 | accounts     |                         |
| /account/token/refresh/       | POST        | JWT 토큰 갱신                 | accounts     | * 프론트에서 처리할때 JS 코드에서 refresh <br> url 부분도  fetch에 포함해주어야 accesstoken을 제대로 반환함 |

- HTTP 메서드 차이에 따라 페이지 특성에 맞게 선택
    - GET 방식 : 데이터를 url에 포함시켜 전달 ex) 정보조회
    - POST 방식 : 데이터를 HTTP요청 본문에 포함시켜 전달 ex) 데이터 제출 및 변경

##  🧶5. 와이어프레임 / UI

- Tool : Uizard

  [![Uizard](https://img.shields.io/badge/Visit-Uizard-yellow?style=flat-square&logo=uizard)](https://uizard.io/)


![image](https://github.com/maxkim77/DRFChatService/assets/141907655/4c51a948-7be2-4cca-8aa0-2ec702a934e7)


![image](https://github.com/maxkim77/DRFChatService/assets/141907655/3a76be2a-41fe-4cd4-be1b-0a7720e1db5a)


![슬라이드1](https://github.com/maxkim77/DRFChatService/assets/141907655/331cc110-a832-4000-8dbe-ed8b74ffbaaa)


##  🖼6. 데이터베이스 모델링:


![Untitled (1)](https://github.com/maxkim77/DRFChatService/assets/141907655/5ae969d2-8250-4723-b751-ea9220bb28b0)
- User Table: CustomUser 모델에서 기본키 id, 고유 필드 email 포함 함.


- Chat Table: role 필드 등 포함 하고, 외래키 id를 통해 사용자 테이블 참조함.


- UserChatRequest Table: UserChatRequest 모델에서 외래키 user_id를 통해 사용자 테이블 참조하고,  요청 수 request_count, 날짜 date 포함.


- Chat 모델과 UserChatRequest 모델에서 user 필드를 통해 사용자 테이블과 다대일 관계

## 7. 개발자 김정원

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

