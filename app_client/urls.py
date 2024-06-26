from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('servicos/', views.OrderViewView.as_view(), name="view_orders"),
    path('cadastro/', views.SignUpClient.as_view(), name="sign_up"),
    path('login/', views.SignInView.as_view(), name="sign_in"),
    path('iniciar_pedido/', views.RequestOrderView.as_view(), name="request_os"),
    path('perfil/', views.ProfileView.as_view(), name="profile"),
    path('perfil/editar/', views.EditProfileView.as_view(), name="edit_profile"),
    path('visualizar/<int:id>/', views.ViewOrder.as_view(), name="view_order"),
    path('avaliar/<int:id>/', views.RateService.as_view(), name="rate_service"),
    path('reabrir_serviço/<int:id>/', views.ReopenService.as_view(), name="reopen_service"),
    path('apagar_serviço/<int:id>/', views.DeleteService.as_view(), name="delete_service"),
]
