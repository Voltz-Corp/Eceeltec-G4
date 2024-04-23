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

    user = Users.objects.get(id=user_id)  # Retrieve the user instance
    product = OrderRequest(
        productbrand=brand,
        productType=type,
        productModel=model,
        otherProductType=other,
        productProblemDescription=description,
        userClient=user  # Assign the user instance
    )
    product.save()
    return product


        
