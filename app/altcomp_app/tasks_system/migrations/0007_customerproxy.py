# Generated by Django 3.2.6 on 2022-01-13 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('tasks_system', '0006_alter_task_repair_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('customers.customer',),
        ),
    ]
