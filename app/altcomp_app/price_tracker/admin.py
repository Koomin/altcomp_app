from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from altcomp_app.devices.admin import LaptopSpecificationAdmin
from altcomp_app.devices.models import LaptopProxy
from altcomp_app.properties.admin import InternalSalesInline, PriceInline, ConfigInline
from altcomp_app.properties.models import Price, CategoryProxy, ShopProxy
from altcomp_app.settings.admin import admin_site


class LaptopAdmin(admin.ModelAdmin):
    inlines = [LaptopSpecificationAdmin, InternalSalesInline, PriceInline]
    fields = (
        ('brand', 'name'), ('manufacturer_code', 'shop_code'), ('external_link',),
        ('shop', 'category', 'availability')
    )
    list_display = ['name', 'brand', 'availability', 'external_price', 'internal_price', 'external_link_list',
                    'internal_link']
    list_filter = ['category']

    def internal_price(self, obj):
        try:
            return f'{obj.price.get(active=True, type=Price.INTERNAL).value} zł'
        except ObjectDoesNotExist:
            return '- zł'

    internal_price.short_description = _('Internal price')

    def external_price(self, obj):
        try:
            return f'{obj.price.get(active=True, type=Price.EXTERNAL).value} zł'
        except ObjectDoesNotExist:
            return '- zł'

    external_price.short_description = _('External price')

    def internal_link(self, obj):
        try:
            return mark_safe(f'<a href="{obj.internal_sales.first().internal_link}" target="_blank">CLICK!</a>')
        except (ObjectDoesNotExist, AttributeError):
            return '-'

    internal_link.short_description = _('Internal link')

    def external_link_list(self, obj):
        return mark_safe(f'<a href="{obj.external_link}" target="_blank">CLICK!</a>')

    external_link_list.short_description = _('External link')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ShopAdmin(admin.ModelAdmin):
    inlines = [ConfigInline]


admin_site.register(ShopProxy, ShopAdmin)
admin_site.register(CategoryProxy, CategoryAdmin)
admin_site.register(LaptopProxy, LaptopAdmin)
