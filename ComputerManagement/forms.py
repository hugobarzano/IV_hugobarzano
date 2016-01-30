from django import forms
from ComputerManagement.serializacion import DispositivoSerializado
from ComputerManagement.models import *
import datetime

class DispositivoForm(forms.ModelForm):
    nombre_dispositivo = forms.CharField(max_length=200, help_text="nombre Dispositivo")
    fabricante = forms.CharField(max_length=200, help_text="fabricante Dispositivo")
    caracteristicas = forms.CharField(max_length=400, help_text="caracteristicas Dispositivo")


    class Meta:
        model = Dispositivo
        fields = ('nombre_dispositivo','fabricante','caracteristicas')

class DonacionForm(forms.ModelForm):
    nombre_solicitante =  models.CharField(max_length=200)
    direccion = forms.CharField(max_length=200, help_text="direcion")
    detalles = forms.CharField(max_length=400, help_text="detalles")

    class Meta:
        model = Donacion
        fields = ('nombre_solicitante','direccion','detalles')

class RecogidaForm(forms.ModelForm):
    dni_donante = models.IntegerField()
    nombre_donante  = forms.CharField(max_length=200, help_text="nombre completo")
    correo_donante  = forms.CharField(max_length=200, help_text="correo electronico")
    direccion_donante  = forms.CharField(max_length=200, help_text="direcion")
    fecha = forms.DateField(initial=datetime.date.today)
    comentario_donante = forms.CharField(max_length=400, help_text="comentario")

    class Meta:
        model = Recogida
        fields = ('dni_donante','nombre_donante','correo_donante','direccion_donante','fecha','comentario_donante')
