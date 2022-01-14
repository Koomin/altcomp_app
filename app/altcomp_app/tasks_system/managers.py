from django.db import models


class TaskClosedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='close')


class TaskOpenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='open')
