# Generated by Django 3.2.6 on 2021-11-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_remove_laptop_internal_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
