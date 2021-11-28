import decimal

from django.http import JsonResponse, HttpResponseRedirect
from django.apps import apps
from django.urls import reverse
from django.utils.safestring import mark_safe

from altcomp_app.notifications.models import Notification


def get_notifications(request):
    if Notification.objects.filter(viewed=False):
        notifications = ''
        for notification in Notification.objects.filter(viewed=False):
            msg = ''
            for key, value in notification.changes.items():
                if key == 'price':
                    msg += f'{key.capitalize()} increase {str(value)}' if decimal.Decimal(value) > 0 else f'{key} drop {str(value)}'
                else:
                    msg += f'{key.capitalize()}: not avaliable' if value is False else f'{key}: avaliable'

            notifications += f'<a href="{notification.link}" class="dropdown-item">{msg}</a>'
    else:
        notifications = '<span class="dropdown-item">No new notifications.</span>'
    return JsonResponse({'html': mark_safe(notifications), 'count': Notification.objects.filter(viewed=False).count()})


def notifications_seen(request):
    model = request.POST.get('obj_model')
    app_label = request.POST.get('obj_app')
    obj_id = request.POST.get('obj')
    model = apps.get_model(app_label, model)
    obj = model.objects.get(pk=obj_id)
    obj.notification.all().update(viewed=True)
    return HttpResponseRedirect(reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.id]))
