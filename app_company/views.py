from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Users
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .utils import register, login
from django.contrib.auth import logout
from rolepermissions.roles import assign_role


class SignView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request, 'app_company/signed.html')
        else:
            return render(request, 'app_company/sign.html')

    def post(self, request):
        if 'logout' in request.POST:
            logout(request)
            return redirect('company:sign')

        password = request.POST.get('password')
        email = request.POST.get('email')
        username=request.POST.get('username')
        
        if 'login' in request.POST: 
            email = request.POST.get('email')
            
            login_result = login(request, email, password)
            if login_result == 1:
                    return redirect('company:list_employees')
            elif login_result == 3:
                return redirect('company:employee_template')
            elif login_result == 0:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('company:sign')
            elif login_result == 2:
                ctx = {'usernameL': username}
                messages.error(request, 'Preencha todos os campos')
                return render(request, 'app_company/sign.html', ctx)

        
        
         
@method_decorator(has_permission_decorator('register_employee'), name='dispatch')
class RegisterEmployeeView(View):
    def get(self, request):
        return render(request, 'app_company/register-employee.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = 'F'
        phone = request.POST.get('phone')
        cep = request.POST.get('cep')
        uf = request.POST.get('uf')
        city = request.POST.get('city')
        neighborhood = request.POST.get('neighborhood')
        address = request.POST.get('address')
        number = request.POST.get('number')
        complement = request.POST.get('complement')
        position = request.POST.get('position')
        dob = request.POST.get('dob')

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Já existe um funcionário com esse nome de usuário.")
            return render(request, 'app_company/register-employee.html')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Esse email já está registrado.")
            return render(request, 'app_company/register-employee.html')

        user = Users(username=username, phone=phone, email=email, password=make_password(password), cep=cep, 
                    uf=uf, city=city, neighborhood= neighborhood, address=address, 
                    number=number, complement=complement, role=role, position=position, dob=dob)
        user.save()
        messages.success(request, "Colaborador registrado com sucesso.")
        return redirect('company:list_employees')

@method_decorator(has_permission_decorator('view_employees'), name='dispatch')
class ListEmployeesView(View):
    def get(self, request):
        employees = Users.objects.filter(role='F')  
        return render(request, 'app_company/list-employees.html', {'employees': employees})

@method_decorator(has_permission_decorator('view_employees'), name='dispatch')    
class DeleteEmployeeView(View):
    def post(self,request, pk): 
        employee = Users.objects.get(pk=pk)
        employee.delete()
        return redirect('company:list_employees')
    
@method_decorator(has_permission_decorator('employee_details'), name='dispatch')
class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Users, pk=pk)
        return render(request, 'app_company/employee-detail.html', {'employee': employee})
    
@method_decorator(has_permission_decorator('fazer_coisas'), name='dispatch')
class EmployeeBasicView(View):
    def get(self, request):
        return render(request, 'app_company/employee-temppage.html')