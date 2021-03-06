# Generated by Django 3.2.6 on 2021-11-05 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_price_type'),
        ('devices', '0005_auto_20211105_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='properties.category'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='manufacturer_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='shop',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='properties.shop'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='shop_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='drive_capacity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='drive_type',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='graphic_card',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='memory',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='processor',
            field=models.CharField(blank=True, max_length=1025),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='screen_resolution',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='laptopspecification',
            name='screen_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
    ]
