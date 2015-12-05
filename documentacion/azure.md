#Creación Máquina virtual Azure

Lo primero que necesitamos es tener cuenta en azure y credito para utilizar sus servicios. Voyu a detallar los pasos a segir para
crear una máquina virtual con ubuntu server 14.04. 

Pinchamos en la pestaña de nuevo proceso y selecionamos maquina virtual ubuntu server 14.04
Le asignamos un nombre al servidor, la cuenta de usuario a la que pertenece, una contraseña y el tipo de supscirción:

![azure_1](https://www.dropbox.com/s/iehvwo5d7lg5jr9/azure_1.png?dl=1)

Debemos elegir el tipo de máuina virtual

![azure_2](https://www.dropbox.com/s/nphcvr9fdigu5it/azure_2.png?dl=1)

El tipo de almacenamiento y demas opciones

![azure_3](https://www.dropbox.com/s/1sn7p5z37duu8h3/azure_3.png?dl=1)

Un resumen con las caracteristicas de la máquina que estamos a punto de crear. 

![azure_4](https://www.dropbox.com/s/g2xmrsr72gowgmm/azure_4.png?dl=1)

Tras esperar un rato, la implementación de la maquina virtual concluye y esta se pone en ejecución:

![azure_5](https://www.dropbox.com/s/m3tmmdzg505zqpj/azure_5.png?dl=1)


#Configuración tráfico de red para la máquina virtual

Para permitir tráfico entrante y saliente a la máquina virtual, he segido este [tutorial](https://azure.microsoft.com/es-es/documentation/articles/virtual-networks-create-nsg-arm-pportal/) creando dos reglas sobre la maquina azure.

Regla entrada:

![azure_entrada](https://www.dropbox.com/s/wqeystwm3bo8ras/azure_entrada.png?dl=1)

Regla salida:

![azure_salida](https://www.dropbox.com/s/n7id95aliuuu15t/azure_salida.png?dl=1)

#Configurar nombre de dominio para la máquina vitual

Para asignarle un nombre de dominio a la máquina virtual, he seguido el siguiente [tutorial](https://azure.microsoft.com/es-es/documentation/articles/virtual-machines-create-fqdn-on-portal/) ha consecuencia de ello, se le ha asignado un nombre de dominio y una nueva ip a la máuina virtual ![dns_azure](https://www.dropbox.com/s/pv6kb6lyrl5ksm2/azure_dns.png?dl=1)
