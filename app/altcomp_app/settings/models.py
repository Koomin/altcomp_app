from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProxy(User):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
