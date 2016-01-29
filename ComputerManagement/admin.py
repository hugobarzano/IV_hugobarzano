from django.contrib import admin
from ComputerManagement.models import *
# Register your models here.

class DispositivoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre_dispositivo',)}

admin.site.register(Donacion)
admin.site.register(Dispositivo)
admin.site.register(Informe)
