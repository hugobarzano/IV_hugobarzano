import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoDjango.settings')
from ComputerManagement.models import *
import django
import datetime

django.setup()

def populate():
    dispositivo1 = add_dispositivo('Aspire','Acer','Mas regulero que el copon')
    add_donacion(dispositivo=dispositivo1,nombre_solicitante="Mercedes alba moyano",direccion="Spain, Granada, camino de ronda,182",detalles="DOnatorrrrr")
    dispositivo2 = add_dispositivo('Pavilion','HP','Maquinon del copon')
    add_donacion(dispositivo=dispositivo2,nombre_solicitante="Hugo Barzano Cruz",direccion="Spain, Granada, rivadavia, 4",detalles="Detalles donacion")
    dispositivo3 = add_dispositivo('machisntos','MAC','Mac de los caros')
    add_donacion(dispositivo=dispositivo3,nombre_solicitante="Un tio que usa un mac",direccion="Spain, Granada, ETSIIT",detalles="Detalles del tio que dona un mac")


    add_recogida(77777777,"sergio Soria Alvarez","soria@gmail.com","Spain, Granada, Pedro antonio, 25","Venid a mi casa a por la chatarrra")
    add_recogida(66666666,"Raul Lopez Arebalo","RaulGay@gmail.com","Spain,Granada, Plaza Einstein","Me sobran los pcssss")


    for dis in Dispositivo.objects.all():
        for d in Donacion.objects.filter(dispositivo=dis):
            print "- {0} - {1}".format(str(dis), str(d))


def add_recogida(dni_donante,nombre_donante,correo_donante,direccion_donante,comentario_donante):
    r = Recogida.objects.get_or_create(dni_donante=dni_donante,nombre_donante=nombre_donante,correo_donante=correo_donante,direccion_donante=direccion_donante,fecha="2016-02-02",comentario_donante=comentario_donante)
    #r.save()
    return r

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
