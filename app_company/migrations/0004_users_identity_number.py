# Generated by Django 5.0.3 on 2024-04-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0003_users_address_users_cep_users_city_users_complement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='identity_number',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
