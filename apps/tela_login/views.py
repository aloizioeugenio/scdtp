from django.shortcuts import render
                   
def funcao_login(request):
    return render(request, 'tela_login.html')

def funcao_tela_inicial(request):
    if request.method == 'GET':
        return render(request, 'tela_inicial.html')