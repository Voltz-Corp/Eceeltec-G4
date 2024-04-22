from django.urls import path
from . import views
app_name = 'company'
urlpatterns = [
    path('', views.SignView.as_view(), name='sign'),
    path('registrar_colaborador/', views.RegisterEmployeeView.as_view(), name='register_employee'),
    path('lista_colaboradores/', views.ListEmployeesView.as_view(), name='list_employees'),
    path('colaborador/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'),
    path('colaboradortemp/',views.EmployeeBasicView.as_view(), name='employee_template'),
]