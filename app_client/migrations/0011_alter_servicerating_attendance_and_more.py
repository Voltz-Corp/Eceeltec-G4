# Generated by Django 5.0.3 on 2024-05-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_client', '0010_servicerating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerating',
            name='attendance',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='notes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='service',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='time',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
    ]
