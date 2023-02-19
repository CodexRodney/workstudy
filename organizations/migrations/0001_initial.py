<<<<<<< HEAD
# Generated by Django 4.1.3 on 2023-01-20 16:59
=======
# Generated by Django 4.1.3 on 2023-02-02 06:01
>>>>>>> main

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('accounts', '__first__'),
=======
        ('accounts', '0001_initial'),
>>>>>>> main
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name="Organization's ID")),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organization name')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name="Organization's creater")),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=150, verbose_name='issue details')),
                ('reported_on', models.DateTimeField(verbose_name='date reported')),
<<<<<<< HEAD
                ('status', models.CharField(choices=[('Argent', 'Argent'), ('Done', 'Done'), ('Pending', 'Pending')], max_length=50, verbose_name='state')),
=======
                ('status', models.CharField(choices=[('Done', 'Done'), ('Argent', 'Argent'), ('Pending', 'Pending')], max_length=50, verbose_name='state')),
>>>>>>> main
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization', verbose_name='organization/lab')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='reported_by')),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
                'ordering': ['-reported_on'],
            },
        ),
    ]
