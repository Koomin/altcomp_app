from django.urls import path

from altcomp_app.notifications import views

app_name = 'notifications'

urlpatterns = [
    path('get_notifications/', views.get_notifications),
    path('notifications_seen/', views.notifications_seen),

]
