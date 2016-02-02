from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ComputerManagement.models import *
from ComputerManagement.serializacion import DispositivoSerializado
from ComputerManagement.forms import *


# Create your views here.

def index (request):
	"""Vista de la pagina principal de la aplicacion.
		En ella se listan las empresas que hay registradas
		Tambien da la opcion de registrar una nueva empresa
	"""
	contexto = {}
	aux={}
	contador=0
	lista_dispositivos = Dispositivo.objects.all()
	lista_solicitudes = Recogida.objects.all()

	contexto['dispositivos'] = lista_dispositivos
	contexto['solicitudes']= lista_solicitudes
	return render(request, 'computermanagement/index.html', contexto)
@csrf_exempt
def dispositivo(request, nombre_slug):
	contexto = {}
	try:
		dispositivo = Dispositivo.objects.get(nombre_slug=nombre_slug)
		contexto['nombre_dispositivo'] = dispositivo.nombre_dispositivo
		donaciones = Donacion.objects.filter(dispositivo=dispositivo)
		contexto['donaciones'] = donaciones
		contexto['dispositivo']=dispositivo
	except Dispositivo.DoesNotExist:
		pass

	return render(request,'computermanagement/dispositivo.html', contexto)


@csrf_exempt
def add_dispositivo(request):
	"""Vista de la funcionalidad de anadir dispositivo.

	"""
	if request.method == 'POST':
		form = DispositivoForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else:
		form = DispositivoForm()
	return render(request, 'computermanagement/add_dispositivo.html', {'form': form})


class JSONResponse(HttpResponse):
	"""
	Un HttpResponse que renderiza su contenido a formato JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Dispositivo_lista(request):
	"""
	Lista todos los dispositivos o crea uno nuevo
	"""
	if request.method == 'GET':
		dispositivos = Dispositivo.objects.all()
		serializador = DispositivoSerializado(dispositivos, many=True)
		return JSONResponse(serializador.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = DispositivoSerializado(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
	return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def Dispositivo_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar un dispositivo
	"""
	try:
		dispositivo = Dispositivo.objects.get(pk=pk)
	except Dispositivo.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
	        serializador = DispositivoSerializado(dispositivo)
		return JSONResponse(serializador.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = DispositivoSerializado(dispositivo, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		dispositivo.delete()
		return HttpResponse(status=204)

@csrf_exempt
def solicitarDonacion(request, nombre_slug):

    try:
        dispositivo = Dispositivo.objects.get(nombre_slug=nombre_slug)
    except Dispositivo.DoesNotExist:
                dispositivo = None

    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            if dispositivo:
				contexto = {}
				donacion = form.save(commit=False)
				print dispositivo.nombre_slug
				donacion.dispositivo = dispositivo
				donacion.save()
				contexto['nombre_dispositivo'] = dispositivo.nombre_dispositivo
				donaciones = Donacion.objects.filter(dispositivo=dispositivo)
				contexto['donaciones'] = donaciones
				contexto['dispositivo']=dispositivo
				return render(request,'computermanagement/dispositivo.html', contexto)

        else:
            print form.errors
    else:
        form = DonacionForm()

    context_dict = {'form':form}
    return render(request, 'computermanagement/donacion.html', context_dict)

@csrf_exempt
def add_recogida(request):

		if request.method == 'POST':
			form = RecogidaForm(request.POST)
			if form.is_valid():
				form.save(commit=True)
				return index(request)
			else:
				print form.errors
		else:
				form = RecogidaForm()
		return render(request, 'computermanagement/add_recogida.html', {'form': form})

@csrf_exempt
def recogida(request, dni_donante):
	contexto = {}
	try:
		recogida = Recogida.objects.get(dni_donante=dni_donante)
		contexto['recogida'] = recogida
	except Recogida.DoesNotExist:
		pass

	return render(request,'computermanagement/recogida.html', contexto)
