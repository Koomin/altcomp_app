from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from altcomp_app.devices.models import AccessoryProxy
from altcomp_app.settings.admin import admin_site

from altcomp_app.tasks_system.models import TaskClosed, TaskOpen, Comment

from altcomp_app.customers.models import CustomerProxy

from altcomp_app.core.admin import HistoryAdmin


class AccessoryAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ('description',)
    extra = 1


class TaskAdmin(HistoryAdmin):
    list_display = ('task_number', 'device_name', 'deadline', 'device_type',
                    'technician', 'status', 'priority', 'duration', 'phone_number', 'created')
    fields = ('device_type', 'device_name',
              'accessories',
              'customer', 'deadline',
              'send_notification', 'priority',
              'fault_description', 'repair_description',
              'estimated_price', 'price',
              'technician', 'registrant',
              'status', 'duration')
    list_display_links = ('device_name',)
    list_filter = ('device_type', 'priority', 'technician')
    inlines = (CommentInline,)

    def task_number(self, obj):
        return obj.pk

    task_number.short_description = _('No.')

    def phone_number(self, obj):
        return obj.customer.phone_number

    phone_number.short_description = _('Phone number')

    def has_delete_permission(self, request, obj=None):
        return False


class TaskClosedAdmin(TaskAdmin):
    readonly_fields = ('device_type', 'device_name',
                       'accessories',
                       'customer', 'deadline',
                       'send_notification', 'priority',
                       'fault_description', 'repair_description',
                       'estimated_price', 'price',
                       'technician', 'registrant',
                       'status',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class TaskOpenAdmin(TaskAdmin):
    list_editable = ('technician', 'status', 'priority', 'duration')


class CustomerAdmin(admin.ModelAdmin):
    pass


admin_site.register(AccessoryProxy, AccessoryAdmin)
admin_site.register(TaskClosed, TaskClosedAdmin)
admin_site.register(TaskOpen, TaskOpenAdmin)
admin_site.register(CustomerProxy, CustomerAdmin)
