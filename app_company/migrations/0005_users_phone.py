# Generated by Django 5.0.3 on 2024-04-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0004_users_identity_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(default='', max_length=15, null=True),
        ),
    ]
