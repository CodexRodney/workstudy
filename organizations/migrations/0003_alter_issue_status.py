<<<<<<< HEAD
# Generated by Django 4.1.3 on 2023-01-20 16:59
=======
# Generated by Django 4.1.3 on 2023-02-02 08:58
>>>>>>> main

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_alter_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
<<<<<<< HEAD
            field=models.CharField(choices=[('Argent', 'Argent'), ('Done', 'Done'), ('Pending', 'Pending')], max_length=50, verbose_name='state'),
=======
            field=models.CharField(choices=[('Done', 'Done'), ('Argent', 'Argent'), ('Pending', 'Pending')], max_length=50, verbose_name='state'),
>>>>>>> main
        ),
    ]
