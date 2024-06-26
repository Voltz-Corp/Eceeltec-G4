# Generated by Django 5.0.3 on 2024-06-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_client', '0012_orderrequest_isreopen_orderrequest_reopen_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='status',
            field=models.CharField(choices=[('EM_ANALISE', 'EM ANÁLISE'), ('AGENDADO', 'AGENDADO'), ('AGUARDANDO_ORCAMENTO', 'AGUARDANDO ORÇAMENTO'), ('AGUARDANDO_CONFIRMACAO', 'AGUARDANDO CONFIRMAÇÃO'), ('ACEITO', 'ACEITO'), ('RECUSADO', 'RECUSADO'), ('CANCELADA', 'CANCELADA'), ('EM_REPARO', 'EM REPARO'), ('AGUARDANDO_PECAS', 'AGUARDANDO PEÇAS'), ('CONSERTO_FINALIZADO', 'CONSERTO FINALIZADO'), ('CANCELADO', 'CANCELADO')], default='EM_ANALISE', max_length=30),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='attendance',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='service',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='servicerating',
            name='time',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
