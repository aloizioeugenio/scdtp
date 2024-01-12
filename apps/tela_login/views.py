from django.shortcuts import render
                   
def funcao_login(request):
    return render(request, 'tela_login.html')
