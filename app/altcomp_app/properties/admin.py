from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from altcomp_app.properties.models import Price, InternalSales, Config, Category
from altcomp_app.settings.admin import admin_site


class PriceInline(GenericStackedInline):
    fields = (('value', 'type', 'created'),)
    readonly_fields = ['type', 'created']
    model = Price
    extra = 1
    max_num = 2

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request).filter(active=True)
        return qs


class InternalSalesInline(GenericStackedInline):
    fields = (('margin', 'internal_link'), ('available_items', 'all_items'))
    extra = 1
    max_num = 1
    model = InternalSales


class ConfigInline(admin.StackedInline):
    list_display = ['data']
    model = Config


class CategoryAdmin(admin.ModelAdmin):
    pass


admin_site.register(Category, CategoryAdmin)
