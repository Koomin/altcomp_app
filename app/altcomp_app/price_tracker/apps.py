from django.apps import AppConfig


class PriceTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'altcomp_app.price_tracker'
    verbose_name = 'Price tracker'