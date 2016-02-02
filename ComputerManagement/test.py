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
        #self.assertEqual(d.fabricante,'fabricante1')
        #self.assertEqual(d.caracteristicas,'caracteristicas1')
        print("Dispositivo Creado Correctamente")
