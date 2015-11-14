from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ComputerManagement.models import Dispositivo


# Create your views here.

def index (request):
	"""Vista de la pagina principal de la aplicacion.
		En ella se listan las empresas que hay registradas
		Tambien da la opcion de registrar una nueva empresa
	"""
	lista_dispositivos = Dispositivo.objects.all()
	context = {'lista_dispositivos': lista_dispositivos}
	return render(request, 'computermanagement/index.html', context)




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
