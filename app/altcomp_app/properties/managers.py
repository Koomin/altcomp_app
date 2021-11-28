from django.db import models


class PriceActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def active(self):
        return self.get_queryset().filter(active=True)

    def inactive(self):
        return self.get_queryset().filter(active=False)
