from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Sobreviventes,Inventario
from django.core import serializers
import json
from django.shortcuts import  get_object_or_404

def sobreviventes(request):
    if request.method == "GET":
        sobrevivente_list = Sobreviventes.objects.all()
        return render(request, 'sobreviventes.html', {'sobreviventes': sobrevivente_list})
    elif request.method =="POST":
        nome =request.POST.get('nome')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        localizacao = request.POST.get('localização')
        item = request.POST.getlist('item')
        quant = request.POST.getlist('quant')
        
        
        sobrevivente = Sobreviventes.objects.filter(nome=nome) 
        
        if sobrevivente.exists():
            return render(request, 'sobreviventes.html', {'nome': nome,'idade': idade, 'sexo':sexo,'localização':localizacao , 'item': zip(item, quant)})  
        
        
        sobrevivente = Sobreviventes(
            nome = nome,
            idade = idade,
            sexo = sexo,
            localizacao = localizacao   
        )
        
        sobrevivente.save()
        
        for item, quant in zip(item, quant):
            itn = Inventario(item=item, quant=quant, sobrevivente=sobrevivente)
            itn.save()
        
        return HttpResponse('TEST')
    
def att_sobrevivente(request):
    id_sobrevivente =  request.POST.get('id_sobrevivente')
    sobrevivente = Sobreviventes.objects.filter(id=id_sobrevivente)
    sobrevivente_json = json.loads(serializers.serialize('json', sobrevivente)) [0]['fields']
    sobrevivente_id = json.loads(serializers.serialize('json', sobrevivente))[0]['pk']
    data = {'sobrevivente': sobrevivente_json, 'sobrevivente_id': sobrevivente_id}
    return JsonResponse(sobrevivente_json)


def update_sobrevivente(request,id):
    body =json.loads(request.body)
    nome = body['nome']
    idade = body['idade']
    sexo = body['sexo']
    localizacao = body['localizacao']
    sobrevivente = get_object_or_404(Sobreviventes, id=id)
    try:
        sobrevivente.nome = nome
        sobrevivente.idade= idade
        sobrevivente.sexo = sexo
        sobrevivente.localizacao = localizacao
        sobrevivente.save()
        return JsonResponse({'status':'200' ,'nome':nome,'idade': idade, 'sexo': sexo, 'localizacao': localizacao})
    except:
        JsonResponse({'status': '500'})