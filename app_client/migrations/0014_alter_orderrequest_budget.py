# Generated by Django 5.0.3 on 2024-06-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_client', '0013_alter_orderrequest_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='budget',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
