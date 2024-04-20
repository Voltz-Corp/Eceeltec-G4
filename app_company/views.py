from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Users
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator



@method_decorator(has_permission_decorator('register_employee'), name='dispatch')
class RegisterEmployeeView(View):
    def get(self, request):
        return render(request, 'app_company/register-employee.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = 'F'  

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Já existe um funcionário com esse nome de usuário.")
            return render(request, 'app_company/register-employee.html')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Esse email já está registrado.")
            return render(request, 'app_company/register-employee.html')

        Users.objects.create_user(
            username=username,
            email=email,
            password=make_password(password),
            role=role
        )
        messages.success(request, "Colaborador registrado com sucesso.")
        return redirect('list_employees')


@method_decorator(has_permission_decorator('view_employees'), name='dispatch')
class ListEmployeesView(View):
    def get(self, request):
        employees = Users.objects.filter(role='F')  
        return render(request, 'app_company/list-employees.html', {'employees': employees})