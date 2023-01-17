from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sobreviventes, Inventario
from sobreviventes.models import Sobreviventes, Inventario

def relatorio_geral(request):
    if request.method == "GET":
        sobreviventes_list = Sobreviventes.objects.all()
        return render(request, 'relatorio_geral.html' ,{'sobreviventes': sobreviventes_list})
    
    elif request.method =="GET":
        item_list = Inventario.objects.all()
        return render(request, 'relatorio_geral.html', {'item': item_list})




    
def att_sobrevivente(request):
    print('teste')
    
    return JsonResponse({"teste": 1})