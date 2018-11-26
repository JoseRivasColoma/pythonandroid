from django.db import models

# Create your models here.
class Tipo(models.Model):
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.descripcion

class Auto(models.Model):
    patente = models.CharField(max_length=45)
    dueno = models.CharField(max_length=45, default='')
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=40)
    ano = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

