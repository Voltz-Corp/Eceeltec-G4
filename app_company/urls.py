from django.urls import path
from . import views

urlpatterns = [
    path('registrar_colaborador/', views.RegisterEmployeeView.as_view(), name='register_employee'),
    path('lista_colaboradores/', views.ListEmployeesView.as_view(), name='list_employees'),
    path('colaborador/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'),
]