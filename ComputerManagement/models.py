from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Dispositivo(models.Model):
	"""Modelado basico de un disposito.

	"""
	nombre_dispositivo = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	caracteristicas = models.CharField(max_length=400)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre_dispositivo)
		super(Dispositivo, self).save(*args, **kwargs)

		def __unicode__(self):
			return self.nombre_dispositivo

class Informe(models.Model):
	"""Modelado basico de un informe

	"""
	dispositivo = models.ForeignKey(Dispositivo)
	detalles = models.CharField(max_length=400)

class Recogida(models.Model):
	"""Modelo basico de una recojida"

	"""
	dni_donante = models.IntegerField()
	nombre_donante = models.CharField(max_length=200)
	correo_donante = models.CharField(max_length=200)
	direccion_donante = models.CharField(max_length=200)
	fecha = models.DateField()
	comentario_donante = models.CharField(max_length=200)

class Donacion(models.Model):
	"Modelo basico de una donacion"
	dispositivo = models.ForeignKey(Dispositivo)
	nombre_solicitante =  models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	detalles = models.CharField(max_length=400)

	def __unicode__(self):
		return self.nombre_solicitante
