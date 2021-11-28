from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from altcomp_app.properties.managers import PriceActive


class Price(models.Model):
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'
    PRICE_TYPES = (
        (INTERNAL, 'Internal'),
        (EXTERNAL, 'External')
    )

    value = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=8, choices=PRICE_TYPES, default=EXTERNAL)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    active = models.BooleanField(default=True)
    objects = PriceActive()

    def __str__(self):
        return self.type


class InternalSales(models.Model):
    margin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    internal_link = models.URLField(blank=True, null=True)
    available_items = models.IntegerField(blank=True)
    all_items = models.IntegerField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = 'Internal sales'


class Shop(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Config(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    data = models.JSONField(
        default={'price': [], 'brand': [], 'manufacturer_code': [], 'shop_code': [], 'availability': []})


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class CategoryProxy(Category):
    class Meta:
        proxy = True
        app_label = 'price_tracker'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ShopProxy(Shop):
    class Meta:
        proxy = True
        app_label = 'price_tracker'
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
