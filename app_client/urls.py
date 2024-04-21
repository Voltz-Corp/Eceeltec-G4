from django.urls import path
from . import views

urlpatterns = {
    path('ver_pedidos/', views.OrderViewView.as_view(), name="view_orders"),
}