from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    preco = models.IntegerField()
    

def __str__(self):
    return self.nome
