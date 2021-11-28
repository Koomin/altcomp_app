from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.utils.safestring import mark_safe

from altcomp_app.notifications.models import Notification, NotificationConfig


def send_notifications():
    message = ''
    for notification in Notification.objects.filter(viewed=False):
        link = mark_safe(
            f'<a href="{mark_safe(notification.link)}" class="changelist-edit">'
            '<i class="material-icons changelist-icon">Show</i></a>'
        )
        message += f'{notification.changes}, {link} <br>'
    try:
        config = NotificationConfig.objects.all().first()
        email_to = config.emails
        send = config.send_mail
    except ObjectDoesNotExist:
        send = False
        email_to = [settings.DEFAULT_TO_EMAIL]
    if message and send:
        send_mail(
            'Altcomp price drop / increase',
            '',
            from_email=None,
            recipient_list=email_to,
            fail_silently=True,
            html_message=message
        )
