# Generated by Django 3.1.3 on 2020-11-19 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_collection_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]