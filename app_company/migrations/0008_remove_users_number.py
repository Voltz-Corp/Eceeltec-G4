# Generated by Django 5.0.3 on 2024-04-24 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0007_users_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='number',
        ),
    ]
