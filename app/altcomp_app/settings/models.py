from django.db import models
from django.contrib.auth.models import User


class UserProxy(User):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
