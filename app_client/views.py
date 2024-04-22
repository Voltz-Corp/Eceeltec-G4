from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
# from django.contrib.auth.hashers import make_password
from .models import Order
# from rolepermissions.decorators import has_permission_decorator
# from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404


#falta o login
class OrderViewView(View):
    def get(self, request):
        # orders_view = Order.objects.filter (user_id=request.user.id)
        # ctx = {
        #     'orders_view': orders_view,
        #     'app_name': 'orders',
        #     'user': request.user,
        # }
        return render(request, 'orders.html')

