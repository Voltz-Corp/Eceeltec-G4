import json
from datetime import datetime

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
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from app_client.models import OrderRequest, ServiceRating
from datetime import datetime, timedelta, date

class SignView(View):
    def get(self, request):
        user = request.user
        id = request.user.id
        userobject = Users.objects.filter(id=id).first()
        if user.is_authenticated and not userobject.role == 'C':
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
                'user': user,
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

        user = order_request.userClient

        status = request.POST.get('status')
        budget = request.POST.get('budget')
        scheduled_date = request.POST.get('scheduled_date')
        today = datetime.now().date()
        max_date = today + timedelta(days=30)
        if status == "EM_ANALISE":
            print("RESULTADO: EM ANALISE")
            if scheduled_date != '':
                scheduled_date = date.fromisoformat(scheduled_date)
                if scheduled_date < today or scheduled_date > max_date:
                    ctx = {
                            "order_request": order_request,
                            "error": {
                            "message": f"A data precisa estar entre {today} e {max_date}!"
                        }
                    }
                    return render(request, "app_company/order-request-detail.html", ctx)
            else:
                ctx = {
                            "order_request": order_request,
                            "error": {
                            "message": f"A data precisa estar entre {today} e {max_date}!"
                        }
                    }
                return render(request, "app_company/order-request-detail.html", ctx)

            status = "AGENDADO"

        # actual_time = datetime.now().date()
        # days_difference = (actual_time - self.closedAt).days


        if (status == "AGUARDANDO_ORCAMENTO" and order_request.status == "AGUARDANDO_ORCAMENTO"):
            print("RESULTADO: AGUARDANDO ORCAMENTO")
            order_request.status = status
            
            if budget:
                if (float(budget.replace(",", ".")) <= 50000):
                    order_request.budget = float(budget.replace(",", "."))
                    order_request.status = "AGUARDANDO_CONFIRMACAO"
                else:
                    ctx = {
                            "order_request": order_request,
                            "errors": {
                            "message": f"O orçamento máximo é R$50.000!"
                            }
                        }
                    return render(request, "app_company/order-request-detail.html", ctx)
            else:
                ctx = {
                            "order_request": order_request,
                            "errors": {
                            "message": f"O orçamento não pode ser vazio"
                            }
                        }
                return render(request, "app_company/order-request-detail.html", ctx)
            
            order_request.save()
            status_display = order_request.get_status_display()
        
            ctx = {
                'name': user.first_name,
                'type': order_request.productType,
                'model': order_request.productModel,
                'status': status_display,
                'statusCode': status,
                'order_id': order_request.id
            }
            
            if budget:
                ctx["budget"] = budget
            html_content = render_to_string('email/emailtemplate.html', ctx)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives('Sua solicitação de serviço foi atualizada', text_content, 'voltzcorporation@gmail.com', [user.username])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            return redirect('company:order_request_details', pk=pk)
        if status=='AGENDADO':
            print("RESULTADO: AGENDADO")
            order_request.status = status
            order_request.scheduled_date=scheduled_date
            order_request.save()
            status_display = order_request.get_status_display()
            ctx = {
                'name': user.first_name,
                'type': order_request.productType,
                'model': order_request.productModel,
                'status': status_display,
                'statusCode': status,
                'date': order_request.scheduled_date,
            }
            if order_request.scheduled_date:
                final_date = order_request.scheduled_date + timedelta(days=7)
                ctx['finaldate'] = final_date

            
            html_content = render_to_string('email/emailtemplate.html', ctx)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives('Sua solicitação de serviço foi atualizada', text_content, 'voltzcorporation@gmail.com', [user.username])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            return redirect('company:order_request_details', pk=pk)
        
        elif order_request.status == 'ACEITO':
            print("RESULTADO: ACEITO")

            order_request = get_object_or_404(OrderRequest, pk=pk)
            order_request.isOs = True
            detailed_problem_description = request.POST.get('detailed_problem_description')
            necessary_parts = request.POST.get('necessary_parts')

            nule_detailed_problem_description = detailed_problem_description.strip()
            nule_necessary_parts = necessary_parts.strip()
            if not nule_detailed_problem_description or len(detailed_problem_description) <= 1:
                ctx = {
                        "order_request": order_request,
                        "error": {
                        "message": f"O campo não pode ser vazio!"
                    }
                }
                return render(request, "app_company/order-request-detail.html", ctx)
            if not nule_necessary_parts or len(necessary_parts) <= 1:
                ctx = {
                        "order_request": order_request,
                        "error": {
                        "message": f"O campo não pode ser vazio!"
                    }
                }
                return render(request, "app_company/order-request-detail.html", ctx)
            order_request.detailedProblemDescription = detailed_problem_description
            order_request.necessaryParts = necessary_parts
            order_request.status = 'EM_REPARO'
            order_request.save()

            status_display = order_request.get_status_display()
            status = order_request.status

            ctx = {
                'name': user.first_name,
                'type': order_request.productType,
                'model': order_request.productModel,
                'status': status_display,
                'statusCode': status,
            }
            print("Display:" + status_display + "Code: " + status)
            html_content = render_to_string('email/emailtemplate.html', ctx)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives('Sua solicitação de serviço foi atualizada', text_content, 'voltzcorporation@gmail.com', [user.username])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            messages.success(request, "Solicitação transformada em ordem de serviço.")
            return redirect('company:order_request_list') # aqui
        
        else:
            print("RESULTADO: ELSE")
            order_request.status = status
            order_request.save()

            status_display = order_request.get_status_display()

            ctx = {
                'name': user.first_name,
                'type': order_request.productType,
                'model': order_request.productModel,
                'status': status_display,
                'statusCode': status,
            }
            html_content = render_to_string('email/emailtemplate.html', ctx)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives('Sua solicitação de serviço foi atualizada', text_content, 'voltzcorporation@gmail.com', [user.username])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            return redirect('company:order_request_details', pk=pk)

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class ServiceOrderDetailView(View):
    def get(self, request, pk):
        previous_url = request.META.get('HTTP_REFERER', '/')
        current_url = request.build_absolute_uri()
        employees = Users.objects.filter(role='F')
        all_orders = OrderRequest.objects.all()

        if current_url == previous_url:
            request.session['previous_url'] = request.session['previous_url']
        else:
            request.session['previous_url'] = previous_url


        ctx = {
            "all_orders": all_orders,
            "employees": employees,
            "previous_url": request.session['previous_url'] 
        }

        try:
            service_order = OrderRequest.objects.get(id=pk)
            ctx['service_order'] = service_order
        except:
            print(None)

        try:
            rating = ServiceRating.objects.get(os=pk)
            ctx['rating'] = rating
        except:
            print(None)


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

        if not service_order.employee and employee:
            service_order.employee_id = employee
        elif service_order.employee and employee and service_order.employee != employee:
            service_order.employee_id = employee

        service_order.save()
        messages.success(request, "Status atualizado.")

        if service_order.status in ['CONSERTO_FINALIZADO']:
            service_order.closedAt = datetime.now()
            service_order.save()

        if assume_order and service_order.status in ['ACEITO', 'EM_REPARO', 'AGUARDANDO_PECAS']:
            service_order.employee = user
            
            service_order.save()
            messages.success(request, "Ordem de serviço atribuída a você.")
        else:
            messages.error(request, "Esta ordem não pode ser atribuída nesta fase.")

        service_order.status = new_status
        service_order.save()

        status_display = service_order.get_status_display()

        ctx = {
            'name': user.first_name,
            'type': service_order.productType,
            'model': service_order.productModel,
            'status': status_display,
            'statusCode': new_status,
        }

        userId = service_order.userClient

        html_content = render_to_string('email/emailtemplate.html', ctx)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives('Sua solicitação de serviço foi atualizada', text_content, 'voltzcorporation@gmail.com', [userId])
        email.attach_alternative(html_content, 'text/html')
        email.send()

        return redirect('company:service_order_details', pk=pk)

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

@method_decorator(has_permission_decorator('os&request_ops'), name='dispatch')
class YourServicesView(View):
    def get(self, request):
        user_id = request.user.id

        orders = OrderRequest.objects.filter(employee_id=user_id)
        serialized_your_orders = serialize("json", orders)
        serialized_your_orders = json.loads(serialized_your_orders)

        ctx = {
            "orders": orders,
            "your_orders_formatted": serialized_your_orders,
        }

        return render(request, 'app_company/your-services.html', ctx)

class DeleteServiceOrder(View):
    def post(self, request, pk):
        order = OrderRequest.objects.get(id=pk)
        order.delete()
        return redirect('company:order_request_list')