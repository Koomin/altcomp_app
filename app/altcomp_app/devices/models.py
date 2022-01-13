import decimal
import requests
from selectolax.parser import HTMLParser

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import models

from altcomp_app.properties.models import Shop, Category, Price, InternalSales
from altcomp_app.notifications.models import Notification

HEADERS = {
    'User-Agent': f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  f'(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


class Accessory(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name

class AccessoryProxy(Accessory):
    class Meta:
        proxy = True
        app_label = 'tasks_system'
        verbose_name = 'Accessory'
        verbose_name_plural = 'Accessories'


class Device(models.Model):
    name = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=12, blank=True)
    model = models.CharField(max_length=255, blank=True)
    manufacturer_code = models.CharField(max_length=255, blank=True)
    shop_code = models.CharField(max_length=255, blank=True)
    availability = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False)
    category = models.ManyToManyField(Category, blank=True)
    external_link = models.URLField()
    price = GenericRelation(Price)
    internal_sales = GenericRelation(InternalSales)
    notification = GenericRelation(Notification)

    class Meta:
        abstract = True

    class UpdateError(Exception):
        pass

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_device_data(self, tree):
        config = self.shop.config.data
        device_data = {}
        for key, value in config.items():
            for css in value:
                try:
                    device_data[key] = tree.css(css)[0].text()
                    break
                except:
                    return False, {}
        return True, device_data


class Laptop(Device):
    def import_external(self):
        response = requests.get(self.external_link, headers=HEADERS)
        if response.status_code == 200:
            tree = HTMLParser(response.content)
            passed, device_data = self.get_device_data(tree)
            if not passed:
                return passed, device_data
            device_data['manufacturer_code'] = device_data['manufacturer_code'].split('|')[1].replace(
                'kod producenta: ', ''),
            device_data['shop_code'] = device_data['shop_code'].split('|')[2].replace('kod x-kom: ', '')
            device_data['price'] = decimal.Decimal(''.join(device_data['price'].split()[:-1]).replace(',', '.'))
            device_data['availability'] = True if device_data['availability'] == 'Dostępny' else False
            return passed, device_data

    def update_external(self):
        response = requests.get(self.external_link, headers=HEADERS)
        changes = {}
        passed = False
        if response.status_code == 200:
            tree = HTMLParser(response.content)
            passed, device_data = self.get_device_data(tree)
            if not passed:
                return passed, changes
            device_data['availability'] = True if device_data['availability'] == 'Dostępny' else False
            device_data['price'] = decimal.Decimal(''.join(device_data['price'].split()[:-1]).replace(',', '.'))
            if device_data['availability'] != self.availability:
                changes['avaliability'] = device_data['availability']
                self.availability = device_data['availability']
            if device_data['price'] != self.price.get(active=True, type=Price.EXTERNAL).value:
                price = self.price.get(active=True, type=Price.EXTERNAL)
                changes['price'] = str(decimal.Decimal(device_data['price']) - price.value)
                price.active = False
                price.save()
                Price.objects.create(content_object=self, value=device_data['price'])
            self.save()
        return passed, changes

    def import_internal(self):
        link = self.internal_sales.first().internal_link
        response = requests.get(link, headers=HEADERS)
        if response.status_code == 200:
            tree = HTMLParser(response.content)
            device_data = {
                'all_items': tree.css('._15mod._1vryf._1t9p2.mqu1_21.mr3m_1')[0].text().split(' ')[1],
                'price': decimal.Decimal(
                    tree.css('._1svub._lf05o.mpof_vs.munh_8.mp4t_4')[0].text().replace(',', '').replace(' ', ''))
            }
            return device_data

    def clean(self, *args, **kwargs):
        super().clean()
        passed, data = self.import_external()
        if not passed:
            raise ValidationError(
                {'external_link': ValidationError('Check configuration - cannot find HTML elements.')})

    def save(self, *args, **kwargs):
        if self._state.adding:
            passed, data = self.import_external()
            if data and passed:
                self.update_data(**data)
                super().save(*args, **kwargs)
                if data.get('price'):
                    Price.objects.create(content_object=self, value=data['price'])
                InternalSales.objects.create(content_object=self, available_items=0, all_items=0)
                Price.objects.create(content_object=self, value=0.00, type=Price.INTERNAL)
        if self.internal_sales.first().internal_link:
            internal_data = self.import_internal()
            if internal_data:
                self.internal_sales.first().all_items = internal_data.get('all_items')
                self.internal_sales.first().save()
                self.price.first().value = internal_data.get('price')
                self.price.first().save()
        super(Laptop, self).save(*args, **kwargs)

    def update_data(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'price':
                continue
            try:
                self._meta.get_field(key)
            except FieldDoesNotExist:
                continue
            setattr(self, key, value)

    def save_and_update(self, **kwargs):
        self.update_data(**kwargs)
        self.save()


class LaptopProxy(Laptop):
    class Meta:
        proxy = True
        app_label = 'price_tracker'
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptops'


class LaptopSpecification(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    memory = models.IntegerField(blank=True)
    processor = models.CharField(max_length=1025, blank=True)
    graphic_card = models.CharField(max_length=255, blank=True)
    drive_capacity = models.IntegerField(blank=True)
    drive_type = models.CharField(max_length=3, blank=True)
    screen_size = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    screen_resolution = models.CharField(max_length=25, blank=True)
    system = models.BooleanField(default=False)
