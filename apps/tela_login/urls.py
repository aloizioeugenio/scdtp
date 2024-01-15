from django.urls import path
from tela_login.views import funcao_login, funcao_tela_inicial

urlpatterns = [
    path('', funcao_login),
    path('tela_inicial/', funcao_tela_inicial, name='abre_tela_inicial')
]