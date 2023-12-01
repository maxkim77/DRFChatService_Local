# ☘ DRF와 Chat Gpt로 만든 영어인터뷰 서비스 - English Max
![cover](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/249439d9-9e83-434d-a556-cd0810e49ff0)

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

✔ Github 프론트 배포, AWS Lightsail 백엔드 배포
### 2.2 배포 및 관련 URL: https://dev.maxworld7070.net/


📍Backend 배포용 : https://github.com/maxkim77/DRFChatService_BE


📍Frontend 배포용 : https://github.com/maxkim77/DRFChatService_FE


##  🎊3. 요구사항 명세와 기능 명세
- Tool : Mindmeister

[![MindMeister](https://img.shields.io/badge/MindMeister-Link-blue.svg)](https://www.mindmeister.com/)


![마인드맵](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/957f93e0-b4a2-4efd-92c7-9662a0330487)


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

  [![Mermaid](https://img.shields.io/badge/Mermaid-Link-blue.svg)](https://mermaid.js.org/)![wbs](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/7bbdc179-facc-427e-b14e-5d787a2a3cf3)



| Scope              | WBS Level | WBS ID | WBS Element Title      | Completion (Completed Date)  |
|--------------------|-----------|--------|------------------------|-------------|
| Planning           | 1         | plan1  | WBS, Model, Requirements| ✅ 11.21. |
| Planning           | 1         | plan2  | ERD                    |  ✅ 11.21. |
| Design             | 2         | des1   | Screen Design          |  ✅ 11.21. |
| Design             | 2         | des2   | URL Design             |  ✅ 11.21. |
| Development        | 3         | dev1   | Page Implementation    |  ✅ 11.22. |
| Development        | 3         | dev2   | CRUD Implementation    |  ✅ 11.22. |
| Development        | 3         | dev3   | User Registration & Login | ✅ 11.25.(일반토큰->JWT 구현에서 시간을 많이 사용)|
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


![플로우차트 drawio](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/f6c122ba-c2f7-4daf-871b-7995c61a0a01)


- 유저 요청에 관한 Pool을 나타낸 플로우 차트
- 각 특징에 맞게 Lane을 구분 함

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

 
📕 **(참고사항)** API 기능과 사용 방법을 명확히 전달 하기 위한 Swegger drf-yasg 사용하여 문서화

![ezgif com-resize (1)](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/a59b4221-c71c-44c4-bd0a-dc2ffcf76405)
- 자동화된 문서 생성
- 인터렉티브한 테스팅 인터페이스

🎁 DRF API Document Pdf : https://drive.google.com/file/d/1kwkup07S1y43iVe64-FYTy0PvZ68nh5c/view?usp=sharing


##  🧶5. 와이어프레임 / UI

- Tool : Uizard


[![Uizard](https://img.shields.io/badge/Visit-Uizard-yellow?style=flat-square&logo=uizard)](https://uizard.io/)


- 와이어 프레임
![5-1](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/f2357d1a-42c0-4463-9e78-00139712a9e2)


- UI
![5-2](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/6b1b465b-4476-4e2c-b882-8d3871f5d09c)


- 실제 구현 화면
![슬라이드1](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/a387b703-9a64-45c5-b6a7-1ec88935462e)


##  🖼6. 데이터베이스 모델링:

![6데이터베이스모델링](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/a0e44d52-3817-4b8e-8a80-8d45947407af)

- User Table: CustomUser 모델에서 기본키 id, 고유 필드 email 포함 함.


- Chat Table: role 필드 등 포함 하고, 외래키 id를 통해 사용자 테이블 참조함.


- UserChatRequest Table: UserChatRequest 모델에서 외래키 user_id를 통해 사용자 테이블 참조하고,  요청 수, 날짜 포함.


- Chat 모델과 UserChatRequest 모델에서 user 필드를 통해 사용자 테이블과 다대일 관계

##  🎨7. 시스템 아키텍처 설계
- Tool : draw.io


[![draw.io](https://img.shields.io/badge/draw.io-Link-blue.svg)](https://app.diagrams.net/)

![시스템아키텍쳐 drawio (3)](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/069e265d-572c-48c0-aae3-8bb1ee27c313)


- AWS Lightsail: (Amazon Web Services의 가상 프라이빗 서버(VPS) 서비스) 서버, 스토리지, 네트워킹, 데이터베이스 관리에 유용.

- Ubuntu: (Linux 기반 운영 체제) 서버 환경에 최적화되어 있으며, 안정성과 보안에 강점을 가짐.

- Gunicorn: (Python WSGI HTTP 서버) Django 애플리케이션 실행과 웹 애플리케이션과 인터넷의 인터페이스 제공에 사용.

- Nginx: (HTTP 및 리버스 프록시 서버) 클라이언트 요청을 Gunicorn 등 애플리케이션 서버로 전달하고 정적 파일 제공.


## 💶8. 개발 전략 및 특징

- '코드의 가치'와 '효율성'을 높이기 위해 아래의 방식을 채택해 개발 함.

![슬라이드1](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/4815490f-b232-4fe0-96d4-1be1cb9b5554)


- TDD : 기능 구현전 테스트 케이스를 먼저 작성하는 방법론
- DRF & Class View : DRF - API 구축을 위한 라이브러리, Class View - View를 정의 할때 클래스로 구성하는 방식
- JWT : Json객체를 사용하여 정보를 안전하게 전송하기 위한 방식
- 특별기능 : AI, Speech to Text

  
## 9. 메인 기능: 주요 기능 및 작동 방식
- 주요 페이지 구현


![10](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/8732cfa5-a4bf-46cf-89a7-0f931a1ea0cc)


- Signup 기능

  
![3](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/16555e9b-0012-4633-8c0c-281b9a89d068)

  
- Login 기능


![1](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/afee7438-e147-4f4f-b593-40c345e6502b)


- Logout 기능


![4](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/5af25ccd-b891-4784-a7b6-6cb94b021eeb)


- Chat Gpt - DRF 연결

![DRF-Chat 연결](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/c9ad61d7-f871-4207-9dd2-d177b3ea6482)

https://github.com/maxkim77/DRFChatService_Local/assets/141907655/44be6060-0727-4092-8fba-c892cfa7abfd


- 로그인을 한 유저만 사용가능


![1](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/71dca268-3629-49c6-ad87-ded780f9ef77)


- 각 유저당 5번 요청 제한


![ezgif com-resize](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/c1cd8dad-c728-44e6-bce2-d8ddea34d006)


- 채팅내역은 데이터베이스 저장 되며 재로그인후 조회 가능


![ezgif com-resize (1)](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/aa069ed9-1b22-4cf5-babd-86ebc7bd78ec)


## 📚 추가 구현 사항

- Github 배포 커스텀 도메인 활성화 / Https 해제

  
![github deploy](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/0576e872-22fd-4d52-a81e-0c7c324b3966)


- Nginx 배포:


    - AWS Lightsail에서 Ubuntu 환경 vscode ssh 연결
    - Django repository git clone
    - Gunicorn 설치 및 연결
    - Nginx 설치 / Gunicorn 연결 및 배포
      

![ezgif com-resize (2)](https://github.com/maxkim77/DRFChatService_Local/assets/141907655/627eb8ec-946c-4deb-bda3-17d0c3644bc4)

* 12.1. 다시 확인해보니 404에러가 떠서 서버점검중

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
    
    - 프론트엔드에서 오류 메시지 처리 후 서버 로그 정상작동 확인

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


 **⚒ 오류 4: Failed to Start A high performance web server and a reverse proxy server**
  - nginx를 재시작 하는 상황에서 오류가 발생해 systemctl status nginx.service 명령어를 통해 확인해 보니 위 오류와 같이 발생함.
  - **해결책:**

    
        - sudo nginx -t 를 통해 파일 문법 검사를 해봄

    
        - nginx.conf 파일 68번째 줄 문제가 있음을 나타내서 확인

    
        - include /etc/nginx/sites-enabled/*; 지시어가 중복되었기 때문에 삭제

    
        - 다시 sudo nginx -t 를 통해 검사해보니 문제가 없어서 서버 재시작

  
 **💡 알게된 점:**

  - 토큰 관련 오류 해결 방법 및 토큰 관리 방식의 차이(JWT vs. Token Authentication)를 알게 됨.
  - 클래스 설정 옵션에서 단일클래스에서 각각 아래와 같이 차이가 있음을 알게 됨.

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
