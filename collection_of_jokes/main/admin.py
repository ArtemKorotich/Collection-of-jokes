from django.contrib import admin
from .models import SiteSetting, UserActionLog

admin.site.register(SiteSetting)
admin.site.register(UserActionLog)