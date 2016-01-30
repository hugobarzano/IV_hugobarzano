import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')
from ComputerManagement.models import *
import django
django.setup()

def populate():
    disposito1 = add_dispositivo('Dispositivo 1','fabricante 1','caracteristicas 1')
    add_donacion(dispositivo=disposito1,nombre_solicitante="Hugo Barzano",direccion="rivadavia numero 4",detalles="Doname algooo")

    for dis in Dispositivo.objects.all():
        for d in Donacion.objects.filter(dispositivo=dis):
            print "- {0} - {1}".format(str(dis), str(d))



def add_donacion(dispositivo, nombre_solicitante, direccion, detalles):
    d = Donacion.objects.get_or_create(dispositivo=dispositivo, nombre_solicitante=nombre_solicitante,direccion=direccion,detalles=detalles)[0]
    d.nombre_solicitante=nombre_solicitante
    d.direccion=direccion
    d.detalles=detalles
    d.save()
    return d

def add_dispositivo(nombre_dispositivo,fabricante,caracteristicas):
    dis = Dispositivo.objects.get_or_create(nombre_dispositivo=nombre_dispositivo,fabricante=fabricante,caracteristicas=caracteristicas)[0]
    return dis

if __name__ == '__main__':
    print "Starting Computer Management population script..."
    populate()
