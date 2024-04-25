from app_company.models import Users
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
import re
from django.contrib.auth import authenticate, login as auth_login

def register(username, email, password):

    if len(username) < 1 or len(password) < 1 or len(email) < 1:
        return 3

    if username.count(' ') == len(username) or email.count(' ') == len(email) or password.count(' ') == len(password):
        return 3
    
    if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return 2
    
    if len(username) > 30 or len(username) < 1:
        return 0
    else:
        if not re.match("^[a-zA-Z0-9]+$", username):
            return 0

    mail = Users.objects.filter(email=email).first()
    if mail:
        return 4

    user = Users.objects.filter(username=username).first()
    if user:
        return 5

    user = Users.objects.create_user(username=username, email=email, password=password)
    user.save()

    return 1

def login(request, email, password):
    user = Users.objects.filter(email=email).first()
   
    if len(email) < 1 or len(password) < 1:
        return 2

    if not user:
        return 0

    auth_login(request, user)
    if user.role == 'A':
        return 1 
    elif user.role == 'F':
        return 3 
    

def handle_validate_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not isinstance(cpf, str) or len(cpf) != 11 or not cpf.isdigit():
        return False

    invalid_cpfs = [
        "00000000000", "11111111111", "22222222222", "33333333333",
        "44444444444", "55555555555", "66666666666", "77777777777",
        "88888888888", "99999999999"
    ]

    if cpf in invalid_cpfs:
        return False

    sum_ = 0
    weights = [11 - i for i in range(1, 10)]
    for digit, weight in zip(cpf[:9], weights):
        sum_ += int(digit) * weight

    rest = (sum_ * 10) % 11
    if rest == 10 or rest == 11:
        rest = 0
    if rest != int(cpf[9]):
        return False

    sum_ = 0
    weights = [12 - i for i in range(1, 11)]
    for digit, weight in zip(cpf, weights):
        sum_ += int(digit) * weight

    rest = (sum_ * 10) % 11
    if rest == 10 or rest == 11:
        rest = 0
    if rest != int(cpf[10]):
        return False

    return True

def validate_inputs(email, phone, cep, dob, username, password, position, identity_number):
    errors = []
    if not re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
        errors.append({
            'field': 'email',
            'message': "Email inválido."
        })

    if len(cep) != 9:  
        errors.append({
            'field': 'cep',
            'message': "CEP inválido. Deve ser uma sequência de 8 dígitos."
        })

    if len(phone) != 15:
        errors.append({
            'field': 'phone',
            'message': "Número de telefone deve ter 11 dígitos."
        })
    
    if not username.strip():
        errors.append({
            'field': 'username',
            'message': "Este campo não pode ser vazio."
        })
    elif len(username) < 2:
        errors.append({
            'field': 'username',
            'message': "Este campo não pode ter menos de 2 caracteres."
        })   
    elif len(username) < 2:
        errors.append({
            'field': 'username',
            'message': "Este campo não pode ter mais de 100 caracteres."
        })     

    if not password.strip():
        errors.append({
            'field': 'password',
            'message': "Este campo não pode ser vazio."
        })

    if not identity_number.strip():
        errors.append({
            'field': 'identity_number',
            'message': "Este campo não pode ser vazio."
        })
    elif len(identity_number) < 14:
        errors.append({
            'field': 'identity_number',
            'message': "Esse campo tem que ter 11 digitos."
        })
    elif not handle_validate_cpf(identity_number):
        errors.append({
            'field': 'identity_number',
            'message': "CPF inválido."
        })

    if not position.strip():
        errors.append({
            'field': 'position',
            'message': "Este campo não pode ser vazio."
        })

    try:
        pass
    except ValueError:
        errors.append("Data de nascimento inválida.")
    return errors
    