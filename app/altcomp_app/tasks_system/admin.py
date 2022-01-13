from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from altcomp_app.devices.models import AccessoryProxy
from altcomp_app.settings.admin import admin_site

from altcomp_app.tasks_system.models import Task, TaskClosed, TaskOpen, Comment

from altcomp_app.customers.models import CustomerProxy


class AccessoryAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ('description',)
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_number', 'device_name', 'deadline', 'device_type',
                    'technician', 'status', 'priority', 'created')
    fields = ('device_type', 'device_name',
              'accessories',
              'customer', 'deadline',
              'send_notification', 'priority',
              'fault_description', 'repair_description',
              'estimated_price', 'price',
              'technician', 'registrant',
              'status',)

    list_filter = ('device_type', 'priority', 'technician')
    list_editable = ('technician', 'status', 'priority')
    inlines = (CommentInline,)

    def task_number(self, obj):
        return obj.pk

    task_number.short_description = _('Task number')

    def has_delete_permission(self, request, obj=None):
        return False


class TaskClosedAdmin(TaskAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(status=Task.Status.CLOSED)

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class TaskOpenAdmin(TaskAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(status=Task.Status.OPEN)


class CustomerAdmin(admin.ModelAdmin):
    pass


admin_site.register(AccessoryProxy, AccessoryAdmin)
admin_site.register(TaskClosed, TaskClosedAdmin)
admin_site.register(TaskOpen, TaskOpenAdmin)
admin_site.register(CustomerProxy, CustomerAdmin)
