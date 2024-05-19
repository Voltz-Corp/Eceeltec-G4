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
    user = authenticate(username=email, password=password)

    if len(email) < 1 or len(password) < 1:
        return 2

    if user is not None:
        login_django(request, user)

        if user.role == 'A':
            return 1 
        elif user.role == 'F':
            return 3
    else:
        return 0 

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

def validate_inputs(username, position, phone, identity_number, email, dob, cep, uf, city, neighborhood, address, complement, password):
    errors = []

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
    elif len(username) > 100:
        errors.append({
            'field': 'username',
            'message': "Este campo não pode ter mais de 100 caracteres."
        })
    if not email.strip():    
        errors.append({
            'field': 'email',
            'message': "Este campo não pode ser vazio."
        })
    elif not re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
        errors.append({
            'field': 'email',
            'message': "Email inválido."
        })
    elif Users.objects.filter(email=email).exists():
        errors.append({
            'field': 'email',
            'message': 'Esse email já está registrado.'
        })

    if not position.strip():
        errors.append({
            'field': 'position',
            'message': "Este campo não pode ser vazio."
        })
    elif len(position) > 100:
        errors.append({
            'field': 'position',
            'message': "Este campo não pode ter mais de 50 caracteres."
        })     
    if not phone.strip():
        errors.append({
            'field': 'phone',
            'message': "Este campo não pode ser vazio."
        })
    elif len(phone) != 15:
        errors.append({
            'field': 'phone',
            'message': "Número de telefone deve ter 11 dígitos."
        })
    elif phone.strip() and not re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', phone):
        errors.append({
            'field': 'phone',
            'message': "Formato de telefone inválido."
        })        

    if not identity_number.strip():
        errors.append({
            'field': 'identity_number',
            'message': "Este campo não pode ser vazio."
        })
    elif len(identity_number) < 14 or len(identity_number) > 20:
        errors.append({
            'field': 'identity_number',
            'message': "Esse campo tem que ter 11 digitos."
        })
    elif identity_number.strip() and not re.match(r'^(\d{3})\.?(\d{3})\.?(\d{3})-?(\d{2})$', identity_number):
        errors.append({ 
            'field': 'identity_number',
            'message': "Formato de CPF inválido."
        })
    elif not handle_validate_cpf(identity_number):
        errors.append({
            'field': 'identity_number',
            'message': "CPF inválido."
        })

    if not dob.strip():
        errors.append({
            'field': 'dob',
            'message': "Este campo não pode ser vazio."
        })
    elif dob.strip() and not re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
        errors.append({
            'field': 'dob',
            'message': 'Formato de data inválido!'
        })
    if not cep.strip():
        errors.append({
            'field': 'cep',
            'message': "Este campo não pode ser vazio."
        })
    elif len(cep) != 9:  
        errors.append({
            'field': 'cep',
            'message': "Este campo deve ser uma sequência de 8 dígitos."
        })
    elif cep.strip() and not re.match(r'^(\d{5})-(\d{3})$', cep):
        errors.append({
            'field': 'cep',
            'message': "Formato de CEP inválido."
        })

    if not uf.strip():
        errors.append({
            'field': 'uf',
            'message': "Este campo não pode ser vazio."
        })
    elif len(uf) > 2 or len(uf) < 2:
        errors.append({
            'field': 'uf',
            'message': "Estado tem que ter exatamente 2 caracteres."
        })
   
    if not city.strip():
        errors.append({
            'field': 'city',
            'message': "Este campo não pode ser vazio."
        })
    elif len(city) > 200:
        errors.append({
            'field': 'city',
            'message': "Cidade não pode ter mais de 200 caracteres."
        }) 
    if not neighborhood.strip():
        errors.append({
            'field': 'neighborhood',
            'message': "Este campo não pode ser vazio."
        })
    elif len(neighborhood) > 200:
        errors.append({
            'field': 'neighborhood',
            'message': "Cidade não pode ter mais de 200 caracteres."
        }) 
    if not address.strip():
        errors.append({
            'field': 'address',
            'message': "Este campo não pode ser vazio."
        })
    elif len(address) > 200:
        errors.append({
            'field': 'address',
            'message': "Cidade não pode ter mais de 200 caracteres."
        }) 

    if len(complement) > 75:
        errors.append({
            'field': 'complement',
            'message': "Cidade não pode ter mais de 75 caracteres."
        }) 
    
    if not password.strip():
        errors.append({
            'field': 'password',
            'message': "Este campo não pode ser vazio."
        })

    try:
        pass
    except ValueError:
        errors.append("Data de nascimento inválida.")
    return errors
    