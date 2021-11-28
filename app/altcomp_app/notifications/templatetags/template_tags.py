from altcomp_app.notifications.models import NotificationConfig
from django import template

register = template.Library()


@register.simple_tag
def get_interval():
    config = NotificationConfig.objects.all().first()
    if config:
        return config.refresh_interval * 60000
    else:
        return 60000


@register.filter
def is_notifications(obj):
    try:
        if not 'device' in obj._meta.db_table:
            return False
        notifications = obj.notification.filter(viewed=False)
        if notifications:
            return True
        return False
    except AttributeError:
        return False


@register.filter
def to_class_name(value):
    try:
        return value.__class__.__name__
    except AttributeError:
        return None


@register.filter
def to_app_name(value):
    try:
        return value._meta.app_label
    except AttributeError:
        return None
