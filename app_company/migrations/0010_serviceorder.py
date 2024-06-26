# Generated by Django 5.0.3 on 2024-05-12 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_client', '0004_orderrequest_budget'),
        ('app_company', '0009_users_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailed_problem_description', models.TextField()),
                ('necessary_parts', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('EM_REPARO', 'Em reparo'), ('AGUARDANDO_PECAS', 'Aguardando peças'), ('CONSERTO_FINALIZADO', 'Conserto finalizado'), ('CANCELADO', 'Cancelado')], default='EM_REPARO', max_length=20)),
                ('order_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='app_client.orderrequest')),
            ],
        ),
    ]
