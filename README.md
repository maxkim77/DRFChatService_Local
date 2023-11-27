# DRFChatService_BE

# ChatGPT를 이용한 챗봇 애플리케이션

## 1. 목표와 기능
### 1.1 목표

### 1.2 기능

- 프론트 프로젝트 확장 기능: OpenAI의 GPT-3.5 모델을 이용한 챗봇 애플리케이션 개발

  
- API 기능: 기존 OpenAI에서 제공하는 API 대신 직접 구축한 서버(DRF:Dangro Rest Framework)를 통해 요청

  
- AI 통합 기능 : HTML/CSS 프로젝트에 AI 댓글 및 답변 기능 통합


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
### 2.3 URL 기획
| URL Pattern       | View              | Name            | Description                |
|-------------------|-------------------|-----------------|----------------------------|
| `user/register/`  | UserRegistration  | `user-register` | Endpoint for user registration. |
| `user/login/`     | UserLogin         | `user-login`    | Endpoint for user login.         |
| `chat/gpt/`       | ChatGPTAPI        | `chat-gpt`      | Endpoint for interacting with ChatGPT API. |
| `user/logout/`    | UserLogout        | `logout`        | Endpoint for user logout.        |

## 3. 요구사항 명세와 기능 명세
### 3.1 기본 요구사항


- DRF 활용: 모든 구현은 Django Rest Framework를 사용하여 진행


- 사용자 인증: 회원가입 및 로그인 기능 구현


- 챗봇 API: Django 서버 내 ChatGPT API 구현


- 사용 제한: 각 사용자는 하루에 최대 5번 요청 가능


- 데이터베이스 관리: 채팅 내역 저장 및 조회 기능


### 3.2 선택 요구사항
- 도메인 및 배포: 개인 도메인 등록 및 HTTPS 적용


- OAuth2 연동: 카카오, GitHub 등 OAuth2 연결


## 4. 프로젝트 구조와 개발 일정
### 4.1 프로젝트 구조
### 4.2 개발일정(WBS)

![Untitled diagram-2023-11-21-043933](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/2d7680fa-3777-4527-8282-635c5b6a5cbf)


| Scope              | WBS Level | WBS ID | WBS Element Title      | Completion  |
|--------------------|-----------|--------|------------------------|-------------|
| Planning           | 1         | plan1  | WBS, Model, Requirements|  ✅|
| Planning           | 1         | plan2  | ERD                    | ✅  |
| Design             | 2         | des1   | Screen Design          | ✅  |
| Design             | 2         | des2   | URL Design             | ✅  |
| Development        | 3         | dev1   | Page Implementation    | ✅  |
| Development        | 3         | dev2   | CRUD Implementation    | 🟩  |
| Development        | 3         | dev3   | User Registration & Login | 🟩 |
| Development        | 3         | dev4   | Unique User Permissions | 🟩 |
| Development        | 3         | dev5   | ChatGPT Integration    | 🟩 |
| UI/UX              | 4         | ui1    | UI Implementation      |🟩  |
| Deployment         | 5         | dep1   | Deployment             |🟩  |
| Final Preparations | 6         | prep1  | Readme Completion      | 🟩 |
| Final Preparations | 6         | prep2  | Presentation Preparation| 🟩  |
| Presentation       | 7         | pres1  | Final Presentation     | 🟩 |



## 5. 역할 분담: 김정원 Back-End Developer
## 6. 와이어프레임 / UI
![1](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/d128d630-e9d2-4076-a28a-cb413e3d22a9)
![2](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/190b0ea7-37d3-46a5-93f7-d7ed391b77ed)

## 7. 데이터베이스 모델링:
![Untitled](https://github.com/maxkim77/DRFChatService_BE/assets/141907655/68982241-41bc-42ca-a472-ba572c44ee93)
## 8. 아키텍처: 시스템 아키텍처 설계
## 9. 메인 기능: 주요 기능 및 작동 방식
## 10. 에러 및 해결: 개발 중 발생한 주요 문제 및 해결 방법
## 11. 개발하며 느낀점: 프로젝트를 통해 얻은 경험 및 느낀 점
