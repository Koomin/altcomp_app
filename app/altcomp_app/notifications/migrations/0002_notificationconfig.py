# Generated by Django 3.2.6 on 2021-11-17 16:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_mail', models.BooleanField(default=False)),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
                ('refresh_interval', models.IntegerField(default=1)),
            ],
        ),
    ]
