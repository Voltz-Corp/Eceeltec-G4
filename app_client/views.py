import re
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from app_company.models import Users
from django.contrib.auth.hashers import make_password
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from .models import OrderRequest, ServiceRating
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .utils import product_verify
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class SignUpClient(View): 
    def get(self, request):
        return render(request, 'session/sign-up.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cep = request.POST.get('cep')
        uf = request.POST.get('uf')
        city = request.POST.get('city')
        neighborhood = request.POST.get('neighborhood')
        address = request.POST.get('address')
        number = request.POST.get('number')
        complement = request.POST.get('complement')

        name_treated = name.strip()
        phone_treated = phone.strip()
        email_treated = email.strip()
        password_treated = password.strip()
        
        if Users.objects.filter(first_name=name).exists():
            messages.error(request, "Um usuário com esse nome já existe.")
            return render(request, 'session/sign-up.html')
        
        if not name_treated:
            messages.error(request, 'O campo de nome não pode ser vazio!')
            return render(request, 'session/sign-up.html')
        elif len(name) < 2:
            messages.error(request, 'O campo de nome não pode ser menor que 2 caracteres!')
            return render(request, 'session/sign-up.html')

        if not phone_treated:
            messages.error(request, 'O campo de telefone não pode ser vazio!')
            return render(request, 'session/sign-up.html')

        if not email_treated:
            messages.error(request, 'O campo de email não pode ser vazio!')
            return render(request, 'session/sign-up.html')
        elif not re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
            messages.error(request, 'Formato de email inválido!')
            return render(request, 'session/sign-up.html')

        if not password_treated:
            messages.error(request, 'O campo de senha não pode ser vazio!')
            return render(request, 'session/sign-up.html')

        # first name é o nome completo
        user = Users(first_name=name, username=email, phone=phone, email=email, password=make_password(password), cep=cep, uf=uf, city=city, neighborhood= neighborhood, address=address, number=number, complement=complement, role="C")
        user.save()
        
        return redirect('client:sign_in')

class SignInView(View):
    def get(self, request):
        return render(request, 'session/sign-in.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if not user:
            messages.error(request, 'Usuário ou senha errados!')
            return redirect('client:sign_in')
        
        if user.role != 'C':
            messages.error(request, 'Você não tem permissão para acessar essa página')
            return redirect('client:sign_in')
        
        auth_login(request, user)
        return redirect('client:view_orders')

class OrderViewView( View):
    def get(self, request):

        orders = OrderRequest.objects.filter(userClient_id=request.user.id)
        ctx = {
            'orders': orders,
            'user': request.user
        }

        return render(request, 'RequestOrder/orders.html', ctx)
        # return render(request, 'RequestOrder/orders.html')

class ViewOrder(View):
    def get(self, request, id):
        order = OrderRequest.objects.filter(id=id).first()
        orders = OrderRequest.objects.filter(userClient_id=request.user.id)
        rating = ServiceRating.objects.filter(id=id).first()

        ctx = {
            "order": order,
            "orders": orders,
            "rating": rating,
        }

        return render(request, 'RequestOrder/vieworder.html', ctx)

    def post(self, request, id):
        order = OrderRequest.objects.filter(id=id).first()
        chosen = request.POST.get('choise')
        status_choices = OrderRequest.STATUS_CHOICES

        if (chosen == "yes"):
            order.status = status_choices[4][0]
        else:
            order.status = status_choices[5][0]

        order.save()

        return redirect('client:view_orders')

class RequestOrderView(View):
    def get(self,request):

        return render(request, 'RequestOrder/create-OS.html')
    def post(self, request):
        productBrand = request.POST.get('productBrand')
        productType = request.POST.get('productType')
        productModel = request.POST.get('productModel')
        productOther = request.POST.get('productOther')
        productDescription = request.POST.get('productDescription')

        user_id = request.user.id
        
        print(user_id)

        product_list = []
        
        errors = product_verify(productBrand, productType, productModel, productOther, productDescription, user_id)
        ctx = {     
            'errors': errors,
            'app_name': 'client',
        }
        if errors:
            if str(type(errors)) != "<class 'app_client.models.OrderRequest'>":
                if 'other' not in errors:
                    ctx['productOther'] = productOther
                if 'brand' not in errors:
                    ctx['productBrand'] = productBrand
                if 'type' not in errors:
                    ctx['productType'] = productType
                if 'model' not in errors:
                    ctx['productModel'] = productModel
                if 'description' not in errors:
                    ctx['productDescription'] = productDescription
                    return render(request, 'RequestOrder/create-OS.html', ctx)
                print(ctx)
            # print(ctx)
            return redirect('client:view_orders')

class ProfileView(View):
    def get(self, request):
        user = request.user
        ctx = {'user': user}
        return render(request, 'session/profile.html', ctx)

class EditProfileView(View):
    def get(self, request):
        user = request.user
        ctx = {'user': user}
        return render(request, 'session/edit_profile.html', ctx)

    def post(self, request):
        
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')
        user.cep = request.POST.get('cep')
        user.uf = request.POST.get('uf')
        user.city = request.POST.get('city')
        user.neighborhood = request.POST.get('neighborhood')
        user.address = request.POST.get('address')
        user.number = request.POST.get('number')
        user.complement = request.POST.get('complement')

        user.save()

        return redirect('client:profile')
        # name = request.POST.get('first_name')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # cep = request.POST.get('cep')
        # uf = request.POST.get('uf')
        # city = request.POST.get('city')
        # neighborhood = request.POST.get('neighborhood')
        # address = request.POST.get('address')
        # number = request.POST.get('number')
        # complement = request.POST.get('complement')

        # user = Users(first_name=name, phone=phone, email=email, cep=cep, uf=uf, city=city, neighborhood=neighborhood, address=address, number=number, complement=complement)
        # user.save()

        # return redirect('client:profile')

class RateService(View):
    def get(self, request, id):
        order = OrderRequest.objects.get(id=id)

        ctx = {
            "order": order,
        }

        try:
            rating = ServiceRating.objects.get(os_id=order.id)
            ctx['rating'] = rating
        except:
            print(None)



        return render(request, 'RequestOrder/rateservice.html', ctx)
    def post(self, request, id):
        if 'edit_rating' in request.POST:
            rating = ServiceRating.objects.get(os_id=id)

            attendance = request.POST.get('attendance')
            service = request.POST.get('service')
            time = request.POST.get('time')
            notes = request.POST.get('notes')

            rating.attendance = attendance
            rating.service = service
            rating.time = time
            rating.notes = notes

            rating.save()
            return redirect('client:view_orders')

        attendance = request.POST.get('attendance')
        service = request.POST.get('service')
        time = request.POST.get('time')
        review_notes = request.POST.get('notes')

        errors = []
        if attendance == None:
            errors.append({
            'field': 'attendance',
            'message' : 'Este campo não pode ser vazio!'
            })
            print('oi!')
        if service == None:
            errors.append({
            'field': 'service',
            'message' : 'Este campo não pode ser vazio!'
            })
        if time == None:
            errors.append({
            'field': 'time',
            'message' : 'Este campo não pode ser vazio!'
            })
        if len(str(review_notes)) > 200:
            errors.append({
            'field': 'review_notes',
            'message' : 'Este campo não pode ser maior que 200 caractéres!'
            })
        if errors != '':
            order = OrderRequest.objects.filter(id=id).first()
            ctx = {
                "order": order,
                "errors": errors
                }
            return render(request, 'RequestOrder/rateservice.html', ctx)
        else:
            rating = ServiceRating(attendance = attendance, time = time, service = service, notes = review_notes, os_id = id)
            rating.save()
    
            return redirect('client:view_orders')

class ReopenService(View):

    def get(self, request, id):
        order = OrderRequest.objects.filter(id=id).first()
        orders_listing = OrderRequest.objects.filter(userClient_id=request.user.id)
        ctx = {
            "order": order,
            "orders": orders_listing
        }

        return render(request, 'RequestOrder/reopen-service.html', ctx)
    
    def post(self, request, id):

        order = OrderRequest.objects.filter(id=id).first()
        status_choices = OrderRequest.STATUS_CHOICES

        order.reopen_time()

        if not order.isReopen:
            order.status = status_choices[7][0]
            order.reopen_at = datetime.now()
            order.isReopen = True
            order.save()

        else:
            messages.error(request, "Essa solicitação não pode ser reaberta")
            return redirect('client:view_orders')
            

        return redirect('client:view_orders')

class DeleteService(View):
    def get(self, request, id):
        order = OrderRequest.objects.filter(id=id).first()
        orders_listing = OrderRequest.objects.filter(userClient_id=request.user.id)
        ctx = {
            "order": order,
            "orders": orders_listing
        }

        return render(request, 'RequestOrder/delete-service.html', ctx) 

    def post(self, request, id):

        order = OrderRequest.objects.filter(id=id).first()

        order.delete()
        
        return redirect('client:view_orders')