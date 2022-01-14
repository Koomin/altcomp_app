from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'altcomp_app.customers'
    verbose_name = _('Customers')
    verbose_name_plural = _('Customers')