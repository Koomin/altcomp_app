from django.db import models
from django.utils.translation import gettext_lazy as _

from altcomp_app.core.models import HistoryModel
from altcomp_app.tasks_system.managers import TaskOpenManager, TaskClosedManager


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
                                    related_name='tasks', verbose_name=_('Device type'))
    device_name = models.CharField(max_length=250, null=False, blank=False, verbose_name=_('Device name'))
    accessories = models.ManyToManyField('devices.Accessory', related_name='tasks', verbose_name=_('Accessories'))
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='tasks', verbose_name=_('Customer'))
    technician = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, related_name='tasks',
                                   verbose_name=_('Technician'))
    registrant = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name=_('Registrant'))
    fault_description = models.TextField(verbose_name=_('Fault description'))
    repair_description = models.TextField(null=True, blank=True, verbose_name=_('Repair description'))
    estimated_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Estimated price'))
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=_('Price'))
    deadline = models.DateField(null=False, blank=False, verbose_name=_('Deadline'))
    status = models.CharField(max_length=5, choices=Status.choices, blank=False, null=False, default=Status.OPEN,
                              verbose_name=_('Status'))
    send_notification = models.CharField(max_length=5, choices=NotificationType.choices, blank=False, null=False,
                                         default=NotificationType.NO, verbose_name=_('Send notification'))
    priority = models.IntegerField(choices=PriorityLevels.choices, blank=False, null=False,
                                   default=PriorityLevels.NORMAL, verbose_name=_('Priority'))


class TaskClosed(Task):
    objects = TaskClosedManager()

    class Meta:
        proxy = True
        verbose_name = _('Closed task')
        verbose_name_plural = _('Closed tasks')


class TaskOpen(Task):
    objects = TaskOpenManager()

    class Meta:
        proxy = True
        verbose_name = _('Open task')
        verbose_name_plural = _('Open tasks')


class Comment(HistoryModel):
    description = models.TextField(verbose_name=_('Description'))
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')