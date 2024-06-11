import os
import django
from datetime import datetime, timedelta

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eceeltec.settings')
django.setup()

from app_client.models import OrderRequest

order_request = OrderRequest.objects.filter().first()

today = datetime.now().date()

order_request.closedAt = today - timedelta(days=31)

order_request.save()