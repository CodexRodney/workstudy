<<<<<<< HEAD
# Generated by Django 4.1.3 on 2023-01-20 16:59
=======
# Generated by Django 4.1.3 on 2023-02-02 06:01
>>>>>>> main

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
<<<<<<< HEAD
            field=models.CharField(choices=[('Pending', 'Pending'), ('Argent', 'Argent'), ('Done', 'Done')], max_length=50, verbose_name='state'),
=======
            field=models.CharField(choices=[('Argent', 'Argent'), ('Pending', 'Pending'), ('Done', 'Done')], max_length=50, verbose_name='state'),
>>>>>>> main
        ),
    ]
