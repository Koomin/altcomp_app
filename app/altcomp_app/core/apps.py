from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = 'altcomp_app.core'
    verbose_name = _('Core')
    verbose_name_plural = _('Core')
