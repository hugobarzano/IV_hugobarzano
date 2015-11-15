from django.test import TestCase
from ComputerManagement.models import Dispositivo, Informe
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.client import RequestFactory
from ComputerManagement.serializacion import DispositivoSerializado


# Create your tests here.



class dispositivoTestCase(TestCase):
	def test_crear_dispositivo(self):
		d = Dispositivo(id_dispositivo=1, nombre_dispositivo='nombre_dispositivo1', fabricante='fabricante1',caracteristicas='caracteristicas dispositivo 1')
		d.save()
		self.assertEqual(d.id_dispositivo,1)
		self.assertEqual(d.nombre_dispositivo,'nombre_dispositivo1')
		print("Dispositivo Creado Correctamente")


class informeTestCase(TestCase):
	def test_crear_informe(self):
		d = Dispositivo(id_dispositivo=1, nombre_dispositivo='nombre_dispositivo1', fabricante='fabricante1',caracteristicas='caracteristicas dispositivo 1')
		d.save()
		i = Informe(dispositivo=d, id_informe=1, detalles='Detalles del informe')
		i.save()
		self.assertEqual(i.dispositivo, d)
		print("Informe Creado Correctamente")

class RutasTests(APITestCase):
	"""
		Clase para testear las rutas de la applicacion
	"""
	def test_detalle_varios_dispositivos(self):
		"""
			Test para consultar varios dispositivos en detalle.
			Metodo get
		"""
		dispositivo = Dispositivo(id_dispositivo=1,nombre_dispositivo='dispositivo1',fabricante='fabricante1',caracteristicas='caracteristicas1')
		dispositivo.save()
		dispositivo2 = Dispositivo(id_dispositivo=2,nombre_dispositivo='dispositivo2',fabricante='fabricante2',caracteristicas='caracteristicas2')
		dispositivo2.save()
		response = self.client.get('/Dispositivos/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content,'[{"id_dispositivo":1,"nombre_dispositivo":"dispositivo1","fabricante":"fabricante1","caracteristicas":"caracteristicas1"},{"id_dispositivo":2,"nombre_dispositivo":"dispositivo2","fabricante":"fabricante2","caracteristicas":"caracteristicas2"}]')
		print("REST: Dispositivos consultados Correctamente")

	def test_crear_dispositivo(self):
		"""
			Test para crear un disposito
			Metodo post
		"""
		data={'id_dispositivo': '3', 'nombre_dispositivo' : 'nombre_post','fabricante' : 'fabricante_post','caracteristicas' : 'caracteristicas_post' }
		response=self.client.post('/Dispositivos/',data, format='json')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(Dispositivo.objects.get().id_dispositivo,3)
		print("REST: Dispositivo creado correctamente")

	def test_detalle_dispositivo(self):
		"""
			Test para consultar un unico dispositivo en detalle.
			Metodo get
		"""
		dispositivo = Dispositivo(id_dispositivo=1,nombre_dispositivo='dispositivo1',fabricante='fabricante1',caracteristicas='caracteristicas1')
		dispositivo.save()
		response = self.client.get('/Dispositivo/1/')
		self.assertEqual(response.content,'{"id_dispositivo":1,"nombre_dispositivo":"dispositivo1","fabricante":"fabricante1","caracteristicas":"caracteristicas1"}')
		print("REST:Dispositivo consultado de manera individual correctamente")

	def test_actualiza_dispositivo(self):
		"""
			Test para actualizar un dispositivo
			Metodo post
		"""
		dispositivo = Dispositivo(id_dispositivo=1,nombre_dispositivo='dispositivo1',fabricante='fabricante1',caracteristicas='caracteristicas1')
		dispositivo.save()
		data={'id_dispositivo' : 1, 'nombre_dispositivo' : 'dispositivo_update', 'fabricante' : 'fabricante_update', 'caracteristicas' : 'caracteristicas_update'}
		response=self.client.post('/Dispositivo/1/',data, format='json')
		self.assertEqual(Dispositivo.objects.get().nombre_dispositivo, 'dispositivo_update')
		self.assertEqual(Dispositivo.objects.get().fabricante, 'fabricante_update')
		self.assertEqual(response.status_code, 202)
        print("REST: Dispositivo actualizado correctamente")

	def test_borra_dispositivo(self):
		"""
			Test para borrar un dispositivo
			Metodo delete
		"""
		dispositivo = Dispositivo(id_dispositivo=1,nombre_dispositivo='dispositivo1',fabricante='fabricante1',caracteristicas='caracteristicas1')
		dispositivo.save()
		response=self.client.delete('/Dispositivo/1/',pk=dispositivo.id_dispositivo)
		self.assertEqual(response.status_code, 204)
        print("REST: Dispositivo borrado correctamente")
