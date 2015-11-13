from rest_framework import serializers
from ComputerManagement.models import Dispositivo

class DispositivoSerializado(serializers.Serializer):
	id_dispositivo = serializers.IntegerField()
	nombre_dispositivo = serializers.CharField(max_length=200)
    fabricante = serializers.CharField(max_length=200)
    caracteristicas = serializers.CharField(max_length=200)

	def create(self, validated_data):
	        """
		Crea y vevuelve una nueva instancia de un Dispositivo
	        """
		return Dispositivo.objects.create(**validated_data)

	def update(self, instance, validated_data):
	        """
	        Actualiza y devuelve una instancia de Dispositivo, teniendo en cuenta los datos validados
	        """
		instance.id_dispositivo = validated_data.get('id_dispositivo', instance.id_dispositivo)
		instance.nombre_dispositivo = validated_data.get('nombre_dispositivo', instance.nombre_dispositivo)
        instance.fabricante = validated_data.get('fabricante', instance.fabricante)
        instance.caracteristicas = validated_data.get('caracteristicas', instance.caracteristicas)
		instance.save()
		return instance
