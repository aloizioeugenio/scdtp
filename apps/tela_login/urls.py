from django.urls import path
from tela_login.views import funcao_login, funcao_tela_inicial, funcao_tela_contratos

urlpatterns = [
    path('', funcao_login),
    path('tela_inicial/', funcao_tela_inicial, name='abre_tela_inicial'),
    path('tela_contratos/', funcao_tela_contratos, name='abre_tela_contratos'),
]