from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresa/', include('app_company.urls')),
    path('cliente/', include('app_client.urls')),
    path('', views.HomeView.as_view(), name="home"),
]
