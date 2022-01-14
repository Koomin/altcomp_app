from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'altcomp_app.settings'
    verbose_name = _('Settings')
    verbose_name_plural = _('Settings')