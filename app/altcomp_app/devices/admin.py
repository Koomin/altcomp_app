from django.contrib import admin
from altcomp_app.devices.models import LaptopSpecification


class LaptopSpecificationAdmin(admin.StackedInline):
    model = LaptopSpecification
    extra = 1
    max_num = 1
