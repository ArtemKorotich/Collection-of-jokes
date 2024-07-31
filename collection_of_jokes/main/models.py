from django.db import models
from django.contrib.auth.models import User

class SiteSetting(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}: {self.value}"

class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"