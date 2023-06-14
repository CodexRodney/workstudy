# Generated by Django 4.1.3 on 2023-06-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_alter_asset_category_type_alter_asset_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed_asset',
            name='student_id',
            field=models.CharField(default='1234', max_length=50, verbose_name='student id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('Not Woking', 'Not Working'), ('Good', 'Good'), ('Faulty', 'Faulty')], max_length=50, verbose_name='asset condition'),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='category',
            field=models.TextField(choices=[('VGA-HDMI Converters', ' VGA-HDMI Converters'), ('HDMI Cables', 'HDMI Cables'), ('Projector', 'Projector'), ('VGA Cables', 'VGA Cables'), ('Others', 'Others')], max_length=50, verbose_name='Asset category name'),
        ),
    ]
