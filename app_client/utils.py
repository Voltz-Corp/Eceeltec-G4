from app_company.models import Users
from .models import OrderRequest

def product_verify(brand, type, model, other, description, user_id):
    errors = []

    if str(type).count(' ') == len(type):
        errors.append({
            'field': 'type',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(type) or len(type) > 75:
        errors.append({
            'field':'type',
            'message': 'Insira de 2 a 75 caracteres!'
            })
    if str(brand).count(' ') == len(brand):
        errors.append({
            'field':'model',
            'message': 'Este campo não pode ser vazio!'
            })
    elif 2 > len(model) or len(model) > 75:
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

    user = Users.objects.get(id=user_id)
    product = OrderRequest(
        productbrand=brand,
        productType=type,
        productModel=model,
        otherProductType=other,
        productProblemDescription=description,
        userClient=user  
    )
    product.save()
    return product

def rating_treatment(attendance, service, time, review_notes):
    errors = []

    if attendance == None or not attendance.strip():
        errors.append({
            'field': 'attendance',
            'message' : 'Este campo não pode ser vazio!'
        })
    if service == None or not service.strip():
        errors.append({
            'field': 'service',
            'message' : 'Este campo não pode ser vazio!'
        })
    if time == None or not time.strip():
        errors.append({
            'field': 'time',
            'message' : 'Este campo não pode ser vazio!'
        })
    if len(str(review_notes)) > 200:
        errors.append({
            'field': 'review_notes',
            'message' : 'Este campo não pode ser maior que 200 caractéres!'
        })
    
    return errors

            
