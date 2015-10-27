from django.test import TestCase
from ComputerManagement.models import Dispositivo, Informe
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
		
	
