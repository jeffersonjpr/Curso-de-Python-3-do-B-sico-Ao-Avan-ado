from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150)


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(max_length=150, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
