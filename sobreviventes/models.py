from django.db import models

class Sobreviventes(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Inventario(models.Model):
    item = models.CharField(max_length=20)
    quant =models.IntegerField() 
    sobrevivente = models.ForeignKey(Sobreviventes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item
    