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
]
