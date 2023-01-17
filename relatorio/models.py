from django.db import models
from sobreviventes.models import Sobreviventes,Inventario




class Sobreviventes(models.Model):
    sobrevivente = models.ForeignKey(Sobreviventes,on_delete=models.CASCADE)
    infectados = models.IntegerField(Sobreviventes)
    n_infectados =models.IntegerField(Sobreviventes)
    agua =models.IntegerField(Inventario)
    alimento =models.IntegerField(Inventario)
    medicamento=models.IntegerField(Inventario)
    municao =models.IntegerField(Inventario)
    
    def __str__(self):
        return self.infectados
    
class Pontos(models.Model):
    pontos =models.IntegerField() 
    infectados = models.ForeignKey(Sobreviventes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pontos
