from django.contrib import admin

from altcomp_app.customers.models import Customer
from altcomp_app.settings.admin import admin_site


class CustomerAdmin(admin.ModelAdmin):
    pass

admin_site.register(Customer, CustomerAdmin)