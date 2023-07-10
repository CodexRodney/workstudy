# Generated by Django 4.1.3 on 2023-07-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_alter_asset_condition_alter_assetcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Borrowed', 'Borrowed'), ('Not available', ' Not available')], max_length=50, verbose_name='asset status'),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='category',
            field=models.TextField(choices=[('Extension/Power Cables', 'Extension/Power Cables'), ('VGA-HDMI Converters', ' VGA-HDMI Converters'), ('VGA Cables', 'VGA Cables'), ('Remote', 'Remote'), ('Projector', 'Projector'), ('HDMI Cables', 'HDMI Cables'), ('Others', 'Others')], max_length=50, verbose_name='Asset category name'),
        ),
    ]
