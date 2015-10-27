from django.db import models

# Create your models here.

class Dispositivo(models.Model):
	id_dispositivo = models.IntegerField()
	nombre_dispositivo = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	caracteristicas = models.CharField(max_length=400)
	
class Informe(models.Model):
	dispositivo = models.ForeignKey(Dispositivo)
	id_informe = models.IntegerField()
	detalles = models.CharField(max_length=400)

