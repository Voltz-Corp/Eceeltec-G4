import json
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Users
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .utils import register, login,validate_inputs, authenticate
from django.contrib.auth import logout, update_session_auth_hash
from rolepermissions.roles import assign_role
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.core.serializers import serialize

from app_client.models import OrderRequest


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
            return redirect('home')

        password = request.POST.get('password')
        email = request.POST.get('email')
        username=request.POST.get('username')
        
        if 'login' in request.POST: 
            email = request.POST.get('email')
            user = authenticate(username=email, password=password)
            if user is None:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('company:sign')
            if user.role != 'F' and user.role != 'A':
                messages.error(request, 'Você não tem permissão para acessar essa página')
                return redirect('Forbidden403')
            login_result = login(request, email, password)
            if login_result == 1:
                return redirect('company:list_employees')
            elif login_result == 3:
                return redirect('company:order_request_list')
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
        identity_number = request.POST.get('identity_number')
        password = request.POST.get('password')
        role = 'F'  
        cep = request.POST.get('cep')
        uf = request.POST.get('uf')
        city = request.POST.get('city')
        neighborhood = request.POST.get('neighborhood')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        complement = request.POST.get('complement')
        position = request.POST.get('position')
        dob = request.POST.get('dob')
        errors = validate_inputs(username, position, phone, identity_number, email, dob, cep, uf, city, neighborhood, address, complement, password)
        ctx = {
            'username': username,
            'email': email,
            'password': password,
            'cep': cep,
            'uf': uf,
            'city': city,
            'neighborhood': neighborhood,
            'address': address,
            'phone': phone,
            'complement': complement,
            'position': position,
            'dob': dob,
            'identity_number': identity_number
        }

        if errors:
            ctx['errors'] = errors
            return render(request, 'app_company/register-employee.html', ctx)
        
        user = Users(
            first_name=username,
            username=email,
            email=email,
            identity_number=identity_number,
            password=make_password(password),
            cep=cep,
            uf=uf,
            city=city,
            neighborhood=neighborhood,
            address=address,
            phone=phone,
            complement=complement,
            role=role,
            position=position,
            dob=None if not dob.strip() else dob
            )
        user.save()
        messages.success(request, "Colaborador registrado com sucesso.")
        return redirect('company:list_employees')
       
@method_decorator(has_permission_decorator('config_p-user'), name='dispatch')
class ConfigEmployeeView(View):
    def get(self, request):
        user = request.user

        if user.password_was_changed == True:
            return render(request, 'app_company/personalize-employee.html')
        else:
            return render(request, 'app_company/personalize-employee.html', {'changed': 0})

        # return render(request, 'app_company/personalize-employee.html')
    
    def post(self, request):
        old_password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        user = request.user

        if not check_password(old_password, user.password):
            messages.error(request, "Senha incorreta")
            if user.password_was_changed == True:
                return render(request, 'app_company/personalize-employee.html')
            else:
                return render(request, 'app_company/personalize-employee.html', {'changed': 0})
        
        user.set_password(new_password)
        user.password_was_changed = True
        user.save()
        update_session_auth_hash(request, user)

        messages.success(request, "Senha alterada com sucesso")
        
        return redirect('company:employee_config')

@method_decorator(has_permission_decorator('view_employees'), name='dispatch')
class ListEmployeesView(View):
    def get(self, request):
        employees = Users.objects.filter(role='F')
        user = request.user
        if (user.password_was_changed == False):
            return redirect('company:employee_config')
        else:
            return render(request, 'app_company/list-employees.html', {'employees': employees})

@method_decorator(has_permission_decorator('view_employees'), name='dispatch')    
class DeleteEmployeeView(View):
    def post(self, request, pk): 
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
        id = request.user.id
        user = Users.objects.filter(id=id).first()
        ctx = {
            'name': user.first_name
        }
        return render(request, 'app_company/employee-temppage.html', ctx)
    
@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class OrderRequestListView(View):
    def get(self, request):
        
        user = request.user
        service_orders_statuses = ['EM_REPARO', 'AGUARDANDO_PECAS', 'CONSERTO_FINALIZADO', 'CANCELADO']
        service_requests_statuses = ['EM_ANALISE', 'AGENDADO', 'AGUARDANDO_ORCAMENTO', 'AGUARDANDO_CONFIRMACAO', 'ACEITO', 'RECUSADO', 'CANCELADA']

       

        service_orders = OrderRequest.objects.filter(status__in=service_orders_statuses)
        service_requests = OrderRequest.objects.filter(status__in=service_requests_statuses)

        all_orders = OrderRequest.objects.all()            
        serialized_all_orders = serialize("json", all_orders)
        serialized_all_orders = json.loads(serialized_all_orders)
         

        if (user.password_was_changed == False):
            return redirect('company:employee_config')
        else:
            ctx = {
                'service_orders': service_orders, 
                'service_requests':service_requests, 
                "all_orders": all_orders,
                "all_orders_formatted": serialized_all_orders,
                'user':user,
            }
            return render(request, 'app_company/list-order-request.html', ctx)
        
@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class OrderRequestDetailView(View):
    def get(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        ctx = {
            "order_request": order_request
        }

        return render(request, 'app_company/order-request-detail.html', ctx)

    def post(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        status = request.POST.get('status')
        budget = request.POST.get('budget')
        
        if (status == 'AGUARDANDO_CONFIRMACAO' or status == "AGUARDANDO_ORCAMENTO"):
            order_request.status = status
            if (budget):
                order_request.budget = float(budget.replace(",", "."))
            order_request.save()
            return redirect('company:order_request_details', pk=pk)
        
        elif order_request.status == 'ACEITO':

            order_request = get_object_or_404(OrderRequest, pk=pk)
            order_request.isOs = True
            detailed_problem_description = request.POST.get('detailed_problem_description')
            necessary_parts = request.POST.get('necessary_parts')
            
            order_request.detailedProblemDescription = detailed_problem_description
            order_request.necessaryParts = necessary_parts
            order_request.status = 'EM_REPARO'
            order_request.save()

            messages.success(request, "Solicitação transformada em ordem de serviço.")
            return redirect('company:order_request_list') # aqui
        
        else:
            order_request.status = status
            order_request.save()
            return redirect('company:order_request_details', pk=pk)

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class ServiceOrderDetailView(View):
    def get(self, request, pk):
        service_order = get_object_or_404(OrderRequest, pk=pk)
        employees = Users.objects.filter(role='F')
        all_orders = OrderRequest.objects.all()

        ctx = {
            "all_orders": all_orders,
            "service_order": service_order,
            "employees": employees
        }

        return render(request, 'app_company/service-order.html', ctx)
    
    def post(self, request, pk):
        user = request.user
        service_order = get_object_or_404(OrderRequest, pk=pk)
        new_status = request.POST.get('status')
        assume_order = 'assume' in request.POST
        employee = request.POST.get('tecnician')
        update_necessary_parts = request.POST.get('necessary_parts')
        update_detailed_problem_description = request.POST.get('detailed_problem_description')
        
        if not new_status:
            messages.error(request, "Status inválido.")
            return redirect('company:service_order_details', pk=pk)

        service_order.status = new_status
        service_order.necessaryParts = update_necessary_parts
        service_order.detailedProblemDescription = update_detailed_problem_description

        service_order.save()
        messages.success(request, "Status atualizado.")

        if assume_order and service_order.status in ['ACEITO', 'EM_REPARO', 'AGUARDANDO_PECAS']:
            service_order.employee = user
            
            service_order.save()
            messages.success(request, "Ordem de serviço atribuída a você.")
        else:
            messages.error(request, "Esta ordem não pode ser atribuída nesta fase.")

        return redirect('company:service_order_details', pk=service_order.pk)

@method_decorator(has_permission_decorator('manage_os'), name='dispatch')
class ManageOrder(View):
    def get(self, request, pk):
        employees = Users.objects.filter(role='F')
        order_request = get_object_or_404(OrderRequest, pk=pk)
        order_request = {
            'id': order_request.id,
            'productType': order_request.productType,
            'productbrand':order_request.productbrand,
            'productModel': order_request.productModel,
            'detailedProblemDescription':order_request.detailedProblemDescription,
            'budget':order_request.budget,
            'necessaryParts':order_request.necessaryParts,
            'status': order_request.get_status_display() ,
            'employee':order_request.employee
        }
        return render(request, 'app_company/edit-order.html', {'order_request': order_request, 'employees': employees})
    
    def post(self,request,pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        parts = request.POST.get("partes")
        tec = request.POST.get("tecnico")

        order_request.necessaryParts = parts
        order_request.employee = tec
        order_request.save()
        return render(request, 'edit-order.html', {'order_request': order_request})

