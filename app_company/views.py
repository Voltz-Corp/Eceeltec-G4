from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('register_employee')
def register_employee(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = Users.objects.create_user(username=name, password=password, role="A")
        return HttpResponse("Criado com sucesso!")