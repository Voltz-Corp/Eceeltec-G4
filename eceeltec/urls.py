from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresa/', include('app_company.urls')),
    path('cliente/', include('app_client.urls')),
]
