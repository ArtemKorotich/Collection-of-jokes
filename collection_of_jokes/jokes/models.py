from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPES = (
        ('joke', 'Joke'),  # Исправлено добавление запятой и закрывающей скобки
        ('image', 'Image'),
    )
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text if self.content_type == 'joke' else self.image.url

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.content}"