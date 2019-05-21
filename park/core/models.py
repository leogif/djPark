from django.db import models

# Create your models here.

class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=200)

class Marca(models.Model):
	nome = models.CharField(max_length=100)

class Veiculo(models.Model):
	marca = models.ForeignKey(Marca)
	placa = models.CharField(max_length=7)
	cor = models.CharField(max_length=15)
	obs = models.TextField()
	# obs == Observações		
