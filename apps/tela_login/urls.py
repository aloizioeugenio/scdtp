from django.urls import path
from tela_login.views import funcao_login

urlpatterns = [
    path('', funcao_login)
]