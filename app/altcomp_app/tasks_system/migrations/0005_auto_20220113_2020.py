# Generated by Django 3.2.6 on 2022-01-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_system', '0004_auto_20220113_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskClosed',
            fields=[
            ],
            options={
                'verbose_name': 'Closed task',
                'verbose_name_plural': 'Closed tasks',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('tasks_system.task',),
        ),
        migrations.CreateModel(
            name='TaskOpen',
            fields=[
            ],
            options={
                'verbose_name': 'Open task',
                'verbose_name_plural': 'Open tasks',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('tasks_system.task',),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('close', 'Closed')], default='open', max_length=5),
        ),
    ]
