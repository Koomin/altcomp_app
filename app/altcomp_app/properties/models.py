from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from altcomp_app.properties.managers import PriceActive


class Price(models.Model):
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'
    PRICE_TYPES = (
        (INTERNAL, _('Internal')),
        (EXTERNAL, _('External'))
    )

    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Value'))
    created = models.DateField(auto_now_add=True, verbose_name=_('Created'))
    type = models.CharField(max_length=8, choices=PRICE_TYPES, default=EXTERNAL, verbose_name=_('Type'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    objects = PriceActive()

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prizes')

    def __str__(self):
        return self.type


class InternalSales(models.Model):
    margin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_('Margin'))
    internal_link = models.URLField(blank=True, null=True, verbose_name=_('Internal link'))
    available_items = models.IntegerField(blank=True, verbose_name=_('Avaliable items'))
    all_items = models.IntegerField(blank=True, verbose_name=_('All items'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = _('Internal sales')
        verbose_name = _('Internal sales')


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.name


class Config(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, verbose_name=_('Shop'))
    data = models.JSONField(
        default={'price': [], 'brand': [], 'manufacturer_code': [], 'shop_code': [], 'availability': []},
        verbose_name=_('Data'))

    class Meta:
        verbose_name = _('Config')
        verbose_name_plural = _('Configs')


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class CategoryProxy(Category):
    class Meta:
        proxy = True
        app_label = 'price_tracker'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class ShopProxy(Shop):
    class Meta:
        proxy = True
        app_label = 'price_tracker'
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')
