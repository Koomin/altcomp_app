# Generated by Django 3.2.6 on 2022-01-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_system', '0005_auto_20220113_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='repair_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
