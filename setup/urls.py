from apps.tela_login.views import funcao_login

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tela_login.urls'))
]
