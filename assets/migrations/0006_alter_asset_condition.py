# Generated by Django 4.1.3 on 2023-02-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_rename_categoty_pic_assetcategory_category_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('Not Woking', 'Not Working'), ('Good', 'Good'), ('Faulty', 'Faulty')], max_length=50, verbose_name='asset condition'),
        ),
    ]
