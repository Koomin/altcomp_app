from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NotificationsConfig(AppConfig):
    name = 'altcomp_app.notifications'
    verbose_name = _('Notifications')
    verbose_name_plural = _('Notifications')
