# Generated by Django 3.2.6 on 2022-01-13 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_accessory'),
        ('tasks_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('devices.accessory',),
        ),
    ]
