from app_company.models import Users
from .models import OrderRequest
def product_verify(brand, type, model, other, description):
    errors = []

    if str(type) == "outro" and str(other).count(' ') == len(other):
        errors.append({
            'field': 'other',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(type) or len(type) > 50:
        errors.append({
            'field':'other',
            'message': 'Insira de 2 a 75 caracteres!'
            })

