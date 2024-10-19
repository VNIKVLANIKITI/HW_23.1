from django.contrib import admin
from users.models import User
# Register your models here.
from config.settings import AUTH_USER_MODEL
admin.site.register(User)
from django.contrib.auth import get_user_model

User = get_user_model()