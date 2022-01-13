from django.db import models
from django.utils.translation import gettext_lazy as _

from altcomp_app.core.models import HistoryModel


class Task(HistoryModel):
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        CLOSED = 'close', _('Closed')

    class NotificationType(models.TextChoices):
        SMS = 'sms', _('SMS')
        EMAIL = 'email', _('E-mail')
        NO = 'no', _('Don\'t notify')

    class PriorityLevels(models.IntegerChoices):
        LOW = 4, _('Low')
        NORMAL = 3, _('Normal')
        IMPORTANT = 2, _('Important')
        CRITICAL = 1, _('Critical')

    device_type = models.ForeignKey('properties.Category', on_delete=models.CASCADE, null=False, blank=False,
                                    related_name='tasks')
    device_name = models.CharField(max_length=250, null=False, blank=False)
    accessories = models.ManyToManyField('devices.Accessory', related_name='tasks')
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='tasks')
    technician = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    registrant = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False)
    fault_description = models.TextField()
    repair_description = models.TextField(null=True, blank=True)
    estimated_price = models.DecimalField(max_digits=12, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    deadline = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=5, choices=Status.choices, blank=False, null=False, default=Status.OPEN)
    send_notification = models.CharField(max_length=5, choices=NotificationType.choices, blank=False, null=False,
                                         default=NotificationType.NO)
    priority = models.IntegerField(choices=PriorityLevels.choices, blank=False, null=False,
                                   default=PriorityLevels.NORMAL)


class TaskClosed(Task):
    class Meta:
        proxy = True
        verbose_name = _('Closed task')
        verbose_name_plural = _('Closed tasks')


class TaskOpen(Task):
    class Meta:
        proxy = True
        verbose_name = _('Open task')
        verbose_name_plural = _('Open tasks')


class Comment(HistoryModel):
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False)
