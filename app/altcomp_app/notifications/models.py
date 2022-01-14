from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    created = models.DateField(auto_now_add=True, verbose_name=_('Created'))
    viewed = models.BooleanField(default=False, verbose_name=_('Viewed'))
    changes = models.JSONField(default=dict, verbose_name=_('Changes'))
    link = models.URLField(verbose_name=_('Link'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return f'{self.created} {self.link}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class NotificationConfig(models.Model):
    send_mail = models.BooleanField(default=False, verbose_name=_('Send E-mail'))
    emails = ArrayField(models.EmailField(), blank=True, null=True, verbose_name=_('Emails'))
    refresh_interval = models.IntegerField(default=1, verbose_name=_('Refresh interval'))

    class Meta:
        verbose_name = _('Notification Config')
        verbose_name_plural = _('Notifications Config')

    def save(self, *args, **kwargs):
        if self._state.adding and NotificationConfig.objects.all().count() < 1:
            super().save(*args, **kwargs)
        elif not self._state.adding:
            super(NotificationConfig, self).save()


class NotificationConfigProxy(NotificationConfig):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = _('Notification Config')
        verbose_name_plural = _('Notifications Config')


class NotificationProxy(Notification):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
