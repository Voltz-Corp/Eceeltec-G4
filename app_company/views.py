from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.hashers import make_password
from .models import Users
from rolepermissions.decorators import has_permission_decorator

from django.contrib.auth.decorators import login_required

from rolepermissions.roles import assign_role

@has_permission_decorator('registrar_colaborador')
def register_employee(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = 'F' 

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Já existe um funcionário com esse nome de usuário.")
            return render(request, 'app_company/registrar_colaborador.html')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Esse email já está registrado.")
            return render(request, 'app_company/registrar_colaborador.html')

        user = Users.objects.create_user(
            username=username,
            email=email,
            password=make_password(password),
            role=role
        ) 
        messages.success(request, "Colaborador registrado com sucesso.")
        return redirect('list_functionaries')
    else:
        return render(request, 'app_company/registrar_colaborador.html')

@login_required
@has_permission_decorator('view_functionaries')
def list_functionaries(request):
    if request.method == 'GET':
        employees = Users.objects.filter(role='F')  
        return render(request, 'app_company/lista_colaboradores.html', {'employees': employees})