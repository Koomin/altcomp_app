from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Notification(models.Model):
    created = models.DateField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
    changes = models.JSONField(default=dict)
    link = models.URLField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.created} {self.link}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class NotificationConfig(models.Model):
    send_mail = models.BooleanField(default=False)
    emails = ArrayField(models.EmailField(), blank=True, null=True)
    refresh_interval = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if self._state.adding and NotificationConfig.objects.all().count() < 1:
            super().save(*args, **kwargs)
        elif not self._state.adding:
            super(NotificationConfig, self).save()


class NotificationConfigProxy(NotificationConfig):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = 'Notification config'
        verbose_name_plural = 'Notifications config'


class NotificationProxy(Notification):
    class Meta:
        proxy = True
        app_label = 'settings'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
