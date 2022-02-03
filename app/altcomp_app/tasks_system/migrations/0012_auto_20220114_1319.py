# Generated by Django 3.2.6 on 2022-01-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_system', '0011_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltask',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='historicaltaskclosed',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='historicaltaskopen',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='task',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Duration'),
        ),
    ]
