from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.SignView.as_view(), name='sign'),
    path('registrar_colaborador/', views.RegisterEmployeeView.as_view(), name='register_employee'),
    path('colaboradores/', views.ListEmployeesView.as_view(), name='list_employees'),
    path('colaborador/<int:pk>/excluir/', views.DeleteEmployeeView.as_view(), name='delete_employee'),
    path('colaborador/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'),
    path('configuracoes/', views.ConfigEmployeeView.as_view(), name='employee_config'),
    path('solicitacoes/', views.OrderRequestListView.as_view(), name='order_request_list'),
    path('solicitacao/<int:pk>/', views.OrderRequestDetailView.as_view(), name='order_request_details'),
    path('confirmar_os/<int:pk>/', views.CreateSOView.as_view(), name='create_os'),
    path('os/<int:pk>/', views.ServiceOrderDetailView.as_view(), name='service_order_details'),
    path('gerenciar_os/<int:pk>/', views.ManageOrder.as_view(), name='manage_order'),
]
