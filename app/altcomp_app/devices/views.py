from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse

from altcomp_app.devices.models import Device
from altcomp_app.notifications.models import Notification


def update_devices(request):
    for obj_class in Device.__subclasses__():
        if obj_class.__subclasses__():
            for obj in obj_class.__subclasses__()[0].objects.all():
                passed, changes = obj.update_external()
                if not passed:
                    return JsonResponse({'data': 'Error, check configuration.', 'status': '0'})
                if changes:
                    link = settings.URL + reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change',
                                                  args=[obj.id])
                    Notification.objects.create(changes=changes, link=link, content_object=obj)
    return JsonResponse({'data': 'Devices updated successfully.', 'status': '1'})
