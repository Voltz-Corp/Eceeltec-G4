from app_company.models import Users
from .models import OrderRequest
def product_verify(brand, type, model, other, description):
    errors = []

    if str(type) == "outro" and str(other).count(' ') == len(other):
        errors.append({
            'field': 'other',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(other) or len(other) > 75:
        errors.append({
            'field':'other',
            'message': 'Insira de 2 a 75 caracteres!'
            })
    if 2 > len(model) or len(model) > 75:
        errors.append({
            'field':'model',
            'message': 'Insira de 2 a 75 caracteres!'
            })
    if str(brand).count(' ') == len(brand):
        errors.append({
            'field':'brand',
            'message': 'Este campo não pode ser vazio!'
            })
    elif 2 > len(brand) or len(brand) > 75:
        errors.append({
            'field':'brand',
            'message': 'Insira de 2 a 75 caracteres!'
            })
    if str(description).count(' ') == len(description):
        errors.append({
            'field':'description',
            'message': 'Este campo não pode ser vazio!'
            })
    elif 2 > len(description) or len(description) > 200:
        errors.append({
            'field':'description',
            'message': 'Insira de 2 a 200 caracteres!'
            })
    
    if len(errors) > 0:
        return errors

    product = OrderRequest(productbrand = brand, productType = type, productModel = model, otherProductType = other, productProblemDescription = description)
    product.save()
    return  product


        
