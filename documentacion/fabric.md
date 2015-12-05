#Utilizando Fabric

Partiendo de una maquina virtual virgen en azure, vamos a realizar el despliegue de la aplicación de manera remota de dos maneras:

**Nota:**Este manual de despliegue, lo he realizado antes de asignarle un nombre de dominio a la maquina virtual sobre la que
trabajo, por lo tanto, la nueva ip del servidor es [](http://104.46.41.50/) y su dominio [](http://computer-management.westeurope.cloudapp.azure.com/) por lo que si desea realizar algun cambio, no olvide utilizar **hugobarzano@104.46.41.50** en lugar de las credenciales que se reflejan mas adelante. 

##Despliegue total sobre maquina anfitriona
Lo primero que vamos a hacer es conectarnos mediante ssh a la maquina virtual azure para poder ir observando los cambios que se van produciendo en ella. 

	ssh hugobarzano@65.52.154.232 -p 22

![fab_1](https://www.dropbox.com/s/jp1oatl3zsuwij8/fab_1.png?dl=1)

Podemos observar que es una anfitrión virgen. Es el momento de prepararlo para albergar nuestra aplicación. 
Lo primero que vamos hacer a modo de prueba es obtener información del host ejecutando:

	 fab -p hugo_1993 -H  hugobarzano@65.52.154.232 informacion_host

Lo que esta ocurriendo es que fabric ejecutara en el host **hugobarzano@65.52.154.232** la accion descrita en **informacion_host** del fichero [fabfile.py](https://github.com/hugobarzano/osl-computer-management/blob/master/fabfile.py) 
env.password.
![fab_2](https://www.dropbox.com/s/x6hfektgoh3eiuk/fab_2.png?dl=1)

Vamos a descargar la aplicacion en la mauina virtual

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 get_aplicacion


Vamos a instalar las dependecnias en la maquina

 	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 instalacion
 
podemos comprobar que la maquina virtual contiene nuestra aplicación

![fab_3](https://www.dropbox.com/s/blqh8x2r67h6h9q/fab_3.png?dl=1)

Sincronizamos los modelos

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 sincronizacion

Ejecutamos los test

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 testeo

Ejecutamos la aplicacion

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 ejecucion

Y comprobamos que esta funcionando mediante **curl http://localhost:80/**

![fab_4](https://www.dropbox.com/s/d28f3o9a7il2uxb/fab_4.png?dl=1)

Llegados a este punto, si tenemos configuradas las reglas para permitir tráfico a traves del puerto 80 para la maquina virtual azure,
la aplicación deberia estar disponible de manera global.
 
##Despliegue docker sobre maquina anfitriona

Si en lugar de realizar el despliegue directamente sobre la maquina, queremos utilizar un contenedor, solo tenemos que ejecutar

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 getDocker

Una vez que se haya instalado docker y se haya descargado la imagen funcional de dockerhub, podemos ejecutar el contenedor

	fab -p hugo_1993 -H  hugobarzano@65.52.154.232 runDocker

	






