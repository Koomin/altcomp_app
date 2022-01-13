from django.db import models
from django.utils.translation import gettext_lazy as _
from altcomp_app.core.models import HistoryModel


class Customer(HistoryModel):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=60, null=False, blank=False)
    phone_number = models.CharField(max_length=9, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CustomerProxy(Customer):
    class Meta:
        proxy = True
        app_label = 'tasks_system'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
