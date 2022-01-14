from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PropertiesConfig(AppConfig):
    name = 'altcomp_app.properties'
    verbose_name = _('Properties')
    verbose_name_plural = _('Properties')