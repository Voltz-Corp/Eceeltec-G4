from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_role = (('A', 'Administrador'),
                    ('F', 'Funcionario'),
                    ('C', 'Cliente'))
    role = models.CharField(max_length=1, choices=choices_role)
