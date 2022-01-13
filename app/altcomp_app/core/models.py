from django.core.exceptions import FieldDoesNotExist
from django.db import models
from simple_history.models import HistoricalRecords


class HistoryModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    def save_and_update(self, *args, **kwargs):
        for key, value in kwargs.items():
            try:
                self._meta.get_field(key)
            except FieldDoesNotExist:
                continue
            setattr(self, key, value)
        self.save()
