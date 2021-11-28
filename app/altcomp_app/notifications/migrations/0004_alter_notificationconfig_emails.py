# Generated by Django 3.2.6 on 2021-11-17 16:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationconfig',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, null=True, size=None),
        ),
    ]
