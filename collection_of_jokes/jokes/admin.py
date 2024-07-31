from django.contrib import admin
from .models import Theme, Content, Favorite

admin.site.register(Theme)
admin.site.register(Content)
admin.site.register(Favorite)