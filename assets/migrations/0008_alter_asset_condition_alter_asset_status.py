# Generated by Django 4.1.3 on 2023-02-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_alter_asset_condition_alter_asset_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('Faulty', 'Faulty'), ('Not Woking', 'Not Working'), ('Good', 'Good')], max_length=50, verbose_name='asset condition'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('Borrowed', 'Borrowed'), ('Not available', ' Not available'), ('Available', 'Available')], max_length=50, verbose_name='asset status'),
        ),
    ]
