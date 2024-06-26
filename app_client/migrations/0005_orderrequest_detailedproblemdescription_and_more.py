# Generated by Django 5.0.3 on 2024-05-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_client', '0004_orderrequest_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrequest',
            name='detailedProblemDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderrequest',
            name='necessaryParts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderrequest',
            name='status',
            field=models.CharField(choices=[('EM_ANALISE', 'Em análise'), ('AGENDADO', 'Agendado'), ('AGUARDANDO_ORCAMENTO', 'Aguardando orçamento'), ('AGUARDANDO_CONFIRMACAO', 'Aguardando confirmação'), ('ACEITO', 'Aceito'), ('RECUSADO', 'Recusado'), ('CANCELADA', 'Cancelada'), ('EM_REPARO', 'Em reparo'), ('AGUARDANDO_PECAS', 'Aguardando peças'), ('CONSERTO_FINALIZADO', 'Conserto finalizado'), ('CANCELADO', 'Cancelado')], default='EM_ANALISE', max_length=30),
        ),
    ]
