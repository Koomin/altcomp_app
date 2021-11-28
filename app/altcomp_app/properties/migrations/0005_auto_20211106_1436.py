# Generated by Django 3.2.6 on 2021-11-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_internalsales'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalsales',
            name='all_items',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internalsales',
            name='available_items',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internalsales',
            name='margin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]