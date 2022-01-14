from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PriceTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'altcomp_app.price_tracker'
    verbose_name = _('Price tracker')
    verbose_name_plural = _('Price tracker')
