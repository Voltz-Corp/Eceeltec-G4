from django.db import models
from django.contrib.auth.models import User,AbstractUser
from app_company.models import Users
class OrderRequest(models.Model):
    STATUS_CHOICES = [
        ('EM_ANALISE', 'Em análise'),
        ('AGENDADO', 'Agendado'),
        ('AGUARDANDO_ORCAMENTO', 'Aguardando orçamento'),
        ('AGUARDANDO_CONFIRMACAO', 'Aguardando confirmação'),
        ('ACEITO', 'Aceito'),
        ('RECUSADO', 'Recusado'),
        ('CANCELADA', 'Cancelada'),
    ]
    productType = models.CharField(max_length=75)
    productbrand = models.CharField(max_length=75)
    productModel = models.CharField(max_length=75)
    productProblemDescription = models.CharField(max_length=200)
    otherProductType = models.CharField(max_length=75)
    userClient = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='EM_ANALISE')


