from django.urls import path

from altcomp_app.devices.views import update_devices

app_name = 'devices'

urlpatterns = [
    path('update_devices/', update_devices)
]
