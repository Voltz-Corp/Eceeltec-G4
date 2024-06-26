# Generated by Django 5.0.3 on 2024-04-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0002_alter_users_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='cep',
            field=models.CharField(default='', max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='city',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='complement',
            field=models.CharField(default='', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='neighborhood',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='number',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='uf',
            field=models.CharField(default='', max_length=2, null=True),
        ),
    ]
