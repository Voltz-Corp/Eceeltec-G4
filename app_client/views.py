from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import OrderRequest
from rolepermissions.decorators import has_permission_decorator
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .utils import Product_verify


#falta o login
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

