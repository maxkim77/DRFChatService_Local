#chat/urls.py
from django.urls import path
from .views import ChatGPTAPI

urlpatterns = [
    path('chat/gpt/', ChatGPTAPI.as_view(), name='chat-gpt'),

]