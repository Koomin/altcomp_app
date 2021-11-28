# Generated by Django 3.2.6 on 2021-11-17 17:19

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0010_alter_laptop_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Laptop',
                'verbose_name_plural': 'Laptops',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('devices.laptop',),
        ),
    ]
