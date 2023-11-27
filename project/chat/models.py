# chat/models.py
from django.db import models
from accounts.models import CustomUser as ChatUser

class Chat(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('assistant', 'Assistant'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} - {self.content}"

class UserChatRequest(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    request_count = models.PositiveIntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
