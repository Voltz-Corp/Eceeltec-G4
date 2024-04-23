import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from app_company.models import Users
from django.contrib.auth.hashers import make_password
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from .models import OrderRequest
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .utils import product_verify
from django.contrib.auth import authenticate, login as auth_login


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
            return messages.error(request, 'O campo de email não pode ser vazio!')
        elif not re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
            messages.error(request, 'Formato de email inválido!')
            return render(request, 'session/sign-up.html')

        if not password_treated:
            return messages.error(request, 'O campo de senha não pode ser vazio!')

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

        auth_login(request, user)
        return redirect('client:view_orders')

class OrderViewView(View):
    def get(self, request):
        
        # orders_view = Order.objects.filter (user_id=request.user.id)
        # ctx = {
        #     'orders_view': orders_view,
        #     'app_name': 'orders',
        #     'user': request.user,
        # }
        return render(request, 'RequestOrder/orders.html')

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
        ctx = {     'errors': errors,
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
            print(ctx)
            return redirect('client:view_orders')

class ProfileView(View):
    def get(self, request):
        user = request.user
        ctx = {'user': user}
        print(user)
        return render(request, 'session/profile.html', ctx)

