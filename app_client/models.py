from django.db import models
from django.contrib.auth.models import User,AbstractUser
from app_company.models import Users
from datetime import datetime, timedelta

class OrderRequest(models.Model):
    STATUS_CHOICES = [
        ('EM_ANALISE', 'EM ANÁLISE'),
        ('AGENDADO', 'AGENDADO'),
        ('AGUARDANDO_ORCAMENTO', 'ORÇAMENTO PENDENTE'),
        ('AGUARDANDO_CONFIRMACAO', 'AGUARDANDO CONFIRMAÇÃO'),
        ('ACEITO', 'ACEITO'),
        ('RECUSADO', 'RECUSADO'),
        ('CANCELADA', 'CANCELADA'),
        ('EM_REPARO', 'EM REPARO'),
        ('AGUARDANDO_PECAS', 'AGUARDANDO PEÇAS'),
        ('CONSERTO_FINALIZADO', 'CONSERTO FINALIZADO'),
        ('CANCELADO', 'CANCELDO'),
    ]
    productType = models.CharField(max_length=75)
    productbrand = models.CharField(max_length=75)
    productModel = models.CharField(max_length=75)
    productProblemDescription = models.CharField(max_length=200)
    otherProductType = models.CharField(max_length=75)
    userClient = models.ForeignKey(Users, on_delete=models.CASCADE)
    employee = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_orders')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='EM_ANALISE')
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    detailedProblemDescription = models.TextField(blank=True, null=True)
    necessaryParts = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    scheduled_date = models.DateField(null=True, blank=True)
    isOs = models.BooleanField(default=False)
    closedAt = models.DateField(blank=True, null=True)
    reopen_at = models.DateField(blank=True, null=True)
    isReopen = models.BooleanField(default=False)

    

    def reopen_time(self):
        actual_time = datetime.now().date()
        days_difference = (actual_time - self.closedAt.date()).days
        if days_difference > 30:
            self.isReopen = True
    
class ServiceRating(models.Model):
    RATINGS = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
]
    attendance = models.IntegerField(choices=RATINGS)
    service = models.IntegerField(choices=RATINGS)
    time = models.IntegerField(choices=RATINGS)
    notes = models.CharField(max_length=200, null=True)

    os = models.ForeignKey(OrderRequest, on_delete=models.CASCADE)