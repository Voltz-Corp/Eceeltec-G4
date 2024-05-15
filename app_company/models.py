from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

class Users(AbstractUser):
    choices_role = (('A', 'Administrador'),
                    ('F', 'Funcionario'),
                    ('C', 'Cliente'))
    position = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=1, choices=choices_role)
    cep = models.CharField(max_length=9, default='', null=True)
    uf = models.CharField(max_length=2, default='', null=True)
    city = models.CharField(max_length=200, default='', null=True)
    neighborhood = models.CharField(max_length=200, default='', null=True)
    address = models.CharField(max_length=200, default='', null=True)
    complement = models.CharField(max_length=75, default='', null=True)
    identity_number = models.CharField(max_length=20, default='', null=True)
    number = models.CharField(max_length=10, default='', null=True)
    phone = models.CharField(max_length=15, default='', null=True)
    dob = models.DateField(null=True, blank=True)
    password_was_changed = models.BooleanField(default=False)

