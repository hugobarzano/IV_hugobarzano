from django.db import models

# Create your models here.

class Dispositivo(models.Model):
	"""Modelado basico de un disposito.

	"""
	id_dispositivo = models.IntegerField()
	nombre_dispositivo = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	caracteristicas = models.CharField(max_length=400)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Dispositivo, self).save(*args, **kwargs)

		def __unicode__(self):
			return self.nombre_dispositivo

class Informe(models.Model):
	"""Modelado basico de un informe

	"""
	dispositivo = models.ForeignKey(Dispositivo)
	id_informe = models.IntegerField()
	detalles = models.CharField(max_length=400)

class Donacion(models.Model):
	"Modelo basico de una donacion"

	dispositivo = models.ForeignKey(Dispositivo)
	id_donacion = models.IntegerField()
	nombre_solicitante =  models.CharField(max_length=200)
	direcion = models.CharField(max_length=200)
	detalles = models.CharField(max_length=400)
