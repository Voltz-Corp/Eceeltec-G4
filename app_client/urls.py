from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.OrderViewView.as_view(), name="view_orders"),
    path('cadastro/', views.SignUpClient.as_view(), name="sign_up"),
    path('login/', views.SignInView.as_view(), name="sign_in"),
    path('solicitar_servico/', views.RequestOrderView.as_view(), name="request_os"),
]
