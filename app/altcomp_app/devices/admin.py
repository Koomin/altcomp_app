from django.contrib import admin
from altcomp_app.devices.models import LaptopSpecification, Accessory
from altcomp_app.settings.admin import admin_site


class LaptopSpecificationAdmin(admin.StackedInline):
    model = LaptopSpecification
    extra = 1
    max_num = 1


class AccessoryAdmin(admin.ModelAdmin):
    pass


admin_site.register(Accessory, AccessoryAdmin)
