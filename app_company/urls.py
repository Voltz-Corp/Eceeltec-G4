from django.urls import path
from . import views

urlpatterns = [
    path('registrar_colaborador/', views.register_employee, name="register_employee"),
    path('lista_colaboradores/', views.list_functionaries, name='list_functionaries'),
]