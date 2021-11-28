from django.conf import settings
from django.urls import reverse

from altcomp_app.devices.models import Device
from altcomp_app.notifications.models import Notification
from altcomp_app.notifications.utils import send_notifications


def update_devices():
    for obj_class in Device.__subclasses__():
        if obj_class.__subclasses__():
            for obj in obj_class.__subclasses__()[0].objects.all():
                passed, changes = obj.update_external()
                link = settings.URL + reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change',
                                              args=[obj.id])
                if not passed:
                    Notification.objects.create(changes={'changes': 'ERROR WHILE IMPORTING'}, link=link,
                                                content_object=obj)
                if changes:
                    Notification.objects.create(changes=changes, link=link, content_object=obj)
    send_notifications()
