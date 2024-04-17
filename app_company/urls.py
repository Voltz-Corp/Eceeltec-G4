from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcionario/', views.register_employee, name="register_employee"),
]