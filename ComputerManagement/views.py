from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ComputerManagement.models import Dispositivo
from ComputerManagement.serializacion import DispositivoSerializado
from ComputerManagement.forms import DispositivoForm


# Create your views here.

def index (request):
	"""Vista de la pagina principal de la aplicacion.
		En ella se listan las empresas que hay registradas
		Tambien da la opcion de registrar una nueva empresa
	"""
	lista_dispositivos = Dispositivo.objects.all()
	context = {'lista_dispositivos': lista_dispositivos}
	return render(request, 'computermanagement/index.html', context)

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
