from django.test import TestCase
from django.test import TestCase
from ComputerManagement.models import *
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.client import RequestFactory
from ComputerManagement.serializacion import DispositivoSerializado

class dispositivoTestCase(TestCase):
	def test_crear_dispositivo(self):
		d = Dispositivo(nombre_dispositivo='nombre_dispositivo1', fabricante='fabricante1',caracteristicas='caracteristicas dispositivo 1')
		d.save()
		self.assertEqual(d.nombre_dispositivo,'nombre_dispositivo1')
		self.assertEqual(d.fabricante,'fabricante1')
		self.assertEqual(d.caracteristicas,'caracteristicas dispositivo 1')
        print("Dispositivo Creado Correctamente")

	def test_remove_dispositivo(self):
		d = Dispositivo(nombre_dispositivo='nombre_dispositivo1', fabricante='fabricante1',caracteristicas='caracteristicas dispositivo 1')
		d.save()
		d.delete()
		self.assertEqual(d.nombre_dispositivo,"nombre_dispositivo1")
		print("Dispositivo eliminado Correctamente")


class recogidaTestCase(TestCase):
	def test_crear_recogida(self):
		r = Recogida(dni_donante=77777777,nombre_donante="nombre test",correo_donante="correo test",direccion_donante="Spain, Granada, Pedro antonio, 25",fecha="2016-02-02", comentario_donante="comentario test")
		r.save()
		self.assertEqual(r.dni_donante,77777777)
		self.assertEqual(r.nombre_donante,"nombre test")
		self.assertEqual(r.correo_donante,'correo test')
		print("Recogida Creada Correctamente")

class donacionTestCase(TestCase):
	def test_crear_donacion(self):
		dis = Dispositivo(nombre_dispositivo='nombre_dispositivo1', fabricante='fabricante1',caracteristicas='caracteristicas dispositivo 1')
		dis.save()
		don = Donacion(dispositivo=dis,nombre_solicitante="nombre test",direccion="direcion test",detalles="detalles test")
		self.assertEqual(don.dispositivo,dis)
		self.assertEqual(don.nombre_solicitante,"nombre test")
		print("Donacion Creada Correctamente")
