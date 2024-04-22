import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from app_company.models import Users
# from django.contrib.auth.hashers import make_password
from .models import Order
# from rolepermissions.decorators import has_permission_decorator
# from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from .models import OrderRequest
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .utils import Product_verify


#falta o login
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

        user = Users(name=name, phone=phone, email=email, password=password, cep=cep, 
                    uf=uf, city=city, neighborhood= neighborhood, address=address, 
                    number=number, complement=complement, role="C")
        user.save()
        
        return render(request, 'session/sign-up.html')

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
        productBrand = request.POST.get('brand')
        productType = request.POST.get('type')
        productModel = request.POST.get('model')
        productOther = request.POST.get('other')
        productDescription = request.POST.get('description')

        user_id = request.user.id

        product_list = []

        errors = Product_verify( productBrand, productType, productModel, productOther, productDescription)

