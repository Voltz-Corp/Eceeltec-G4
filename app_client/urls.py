from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.OrderViewView.as_view(), name="view_orders"),
    path('iniciar_pedido/', views.RequestOrderView.as_view(), name="Request_OS"),

]