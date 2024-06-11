import os
import django

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eceeltec.settings')
django.setup()

from app_company.models import Users

Users.objects.all().delete()
print("Todos os usuários foram deletados.")

def create_admin(username, first_name, email, password):
    if not Users.objects.filter(username=username).exists():
        user = Users.objects.create_user(username=username, first_name=first_name, email=email, password=password, role='A')
        user.save()

username = "eceel-Tec@eceeltec.com"
first_name = "Cláudio"
email = "eceel-Tec@eceeltec.com"
password = "obGWjpaTayKJWpBiFSMm"

create_admin(username, first_name, email, password)