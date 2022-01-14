from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from django.views.decorators.cache import never_cache

from altcomp_app.notifications.models import NotificationConfigProxy, NotificationProxy
from altcomp_app.devices.models import Laptop

from altcomp_app.settings.models import UserProxy

from altcomp_app.tasks_system.models import TaskOpen, TaskClosed


class AltcompAdmin(AdminSite):
    site_header = 'Monty Python administration'
    index_template = 'index.html'

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        return app_list

    @never_cache
    def index(self, request, extra_context=None):
        context = {**self.each_context(request),
                   'title': 'Dashboard',
                   'notifications': NotificationProxy.objects.filter(viewed=False),
                   'notifications_count': NotificationProxy.objects.all().count(),
                   'laptops_count': Laptop.objects.all().count(),
                   'open_tasks_count': TaskOpen.objects.all().count(),
                   'closed_tasks_count': TaskClosed.objects.all().count(),
                   **(extra_context or {}), }
        return TemplateResponse(request, 'index.html', context)


admin_site = AltcompAdmin(name='altcomp_admin')


class NotificationConfigAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    fields = (('send_mail', 'emails'), ('refresh_interval'))

    def has_add_permission(self, request):
        if NotificationConfigProxy.objects.all().count() >= 1:
            return False
        return True


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('created', 'link_click', 'viewed')
    fields = ('created', 'link', 'changes', 'viewed')
    readonly_fields = ('created', 'link', 'changes')

    def link_click(self, obj):
        return mark_safe(
            f'<a href="{obj.link}" class="changelist-edit">' '<i class="material-icons changelist-icon">edit</i></a>'
        )

    link_click.short_description = 'Link'


class UserAdmin(admin.ModelAdmin):
    pass


admin_site.register(NotificationProxy, NotificationAdmin)
admin_site.register(NotificationConfigProxy, NotificationConfigAdmin)
admin_site.register(UserProxy, UserAdmin)
