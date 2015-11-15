from django import forms
from ComputerManagement.serializacion import DispositivoSerializado
from ComputerManagement.models import Dispositivo

class DispositivoForm(forms.ModelForm):
    id_dispositivo = forms.IntegerField()
    nombre_dispositivo = forms.CharField(max_length=200, help_text="nombre Dispositivo")
    fabricante = forms.CharField(max_length=200, help_text="fabricante Dispositivo")
    caracteristicas = forms.CharField(max_length=400, help_text="caracteristicas Dispositivo")


    class Meta:
        model = Dispositivo
        fields = ('id_dispositivo','nombre_dispositivo','fabricante','caracteristicas')
