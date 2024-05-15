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
            if user.role != 'F' and user.role != 'A':
                messages.error(request, 'Você não tem permissão para acessar essa página')
                return redirect('company:sign')
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
        service_orders_data = [{
            'id': so.id,
            'productType': so.productType,
            'productModel': so.productModel,
            'status': so.get_status_display()  
        } for so in service_orders]
        service_requests_data = [{
            'id': request.id,
            'productType': request.productType,
            'productModel': request.productModel,
            'status': request.get_status_display()  
        } for request in service_requests]


        if (user.password_was_changed == False):
            return redirect('company:employee_config')
        else:
            return render(request, 'app_company/list-order-request.html', { 'service_orders': service_orders_data, 'service_requests':service_requests_data, 'user':user})
        
@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class OrderRequestDetailView(View):
    def get(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        order_request_data={
            'id': order_request.id,
            'productType': order_request.productType,
            'productbrand':order_request.productbrand,
            'productProblemDescription':order_request.productProblemDescription,
            'productModel': order_request.productModel,
            'status': order_request.get_status_display()  
        }
        return render(request, 'app_company/order-request-detail.html', {'order_request': order_request_data})

    def post(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        status = request.POST.get('status')
        budget = request.POST.get('budget')
        
        if status == 'ACEITO' and budget:
            order_request.status = status
            order_request.budget = budget
            order_request.save()
            return redirect('company:create_os', pk=order_request.pk)
        else:
            order_request.status = status
            order_request.save()
            return redirect('company:order_request_details', pk=pk)

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class CreateSOView(View):
    def get(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        if order_request.status == 'ACEITO':
            return render(request, 'app_company/create-os.html', {'order_request': order_request})
        else:
            return redirect('company:service_order_details', pk=pk)

    def post(self, request, pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        detailed_problem_description = request.POST.get('detailed_problem_description')
        necessary_parts = request.POST.get('necessary_parts')
        budget = order_request.budget

        if budget > 50000:
            messages.error(request, "Orçamento não pode ser maior que R$50,000.00")
            return redirect('company:create_os', pk=pk)

        order_request.detailedProblemDescription = detailed_problem_description
        order_request.necessaryParts = necessary_parts
        order_request.status = 'EM_REPARO'
        order_request.save()

        messages.success(request, "Solicitação transformada em ordem de serviço.")
        return redirect('company:service_order_details', pk=order_request.pk)

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class ServiceOrderDetailView(View):
    def get(self, request, pk):
        service_order = get_object_or_404(OrderRequest, pk=pk)
        service_order_data={
            'id': service_order.id,
            'productType': service_order.productType,
            'productbrand':service_order.productbrand,
            'productModel': service_order.productModel,
            'detailedProblemDescription':service_order.detailedProblemDescription,
            'budget':service_order.budget,
            'necessaryParts':service_order.necessaryParts,
            'status': service_order.get_status_display() ,
            'employee':service_order.employee
        }
        return render(request, 'app_company/service-order.html', {'service_order': service_order_data})
    def post(self, request, pk):
        service_order = get_object_or_404(OrderRequest, pk=pk)
        new_status = request.POST.get('status')
        assume_order = 'assume' in request.POST
        if not new_status:
            messages.error(request, "Status inválido.")
            return redirect('company:service_order_details', pk=pk)

        service_order.status = new_status
        service_order.save()
        messages.success(request, "Status atualizado.")

        if assume_order and service_order.status in ['ACEITO', 'EM_REPARO']:
            service_order.employee = request.user
            service_order.save()
            messages.success(request, "Ordem de serviço atribuída a você.")
        else:
            messages.error(request, "Esta ordem não pode ser atribuída nesta fase.")

        return redirect('company:service_order_details', pk=service_order.pk)

        
        
@method_decorator(has_permission_decorator('manage_os'), name='dispatch')
class ManageOrder(View):
    def get(self,request,pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        return render(request, 'edit_order.html', {'order_request': order_request})
    
    def post(self,request,pk):
        order_request = get_object_or_404(OrderRequest, pk=pk)
        parts = request.POST.get("partes")
        status = status = request.POST.get('status')
        tec = request.POST.get("tecnico")
        
        if not parts and not tec:
            order_request.status = status
            order_request.save()
            return render(request, 'edit_order.html', {'order_request': order_request})
        
        elif not parts:
            order_request.status = status
            order_request.tec = tec
            order_request.save()
            return render(request, 'edit_order.html', {'order_request': order_request})
        
        elif not tec:
            order_request.status = status
            order_request.parts = parts
            order_request.save()
            return render(request, 'edit_order.html', {'order_request': order_request})
        
        order_request.parts = parts
        order_request.tec = tec
        order_request.save()
        return render(request, 'edit_order.html', {'order_request': order_request})

