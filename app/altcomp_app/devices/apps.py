from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DevicesConfig(AppConfig):
    name = 'altcomp_app.devices'
    verbose_name = _('Device')
    verbose_name_plural = _('Devices')
