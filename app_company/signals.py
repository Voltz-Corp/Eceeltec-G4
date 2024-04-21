from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.role == "A":
            assign_role(instance, 'administrador')
        elif instance.role == "F":
            assign_role(instance, 'funcionario')
        elif instance.role == "C":
            assign_role(instance, 'cliente')
