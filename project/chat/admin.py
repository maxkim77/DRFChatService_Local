from django.contrib import admin
from .models import Chat, UserChatRequest

admin.site.register(Chat)
admin.site.register(UserChatRequest)
