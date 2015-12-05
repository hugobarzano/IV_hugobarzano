# OSL Computer Management

##Proyecto para Infraestructura Virtual 2015/2016
[![Build Status](https://travis-ci.org/hugobarzano/osl-computer-management.svg?branch=master)](https://travis-ci.org/hugobarzano/osl-computer-management) [![Build Status](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master/build_image)](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://computer-management.herokuapp.com/)
[![Azure](https://www.dropbox.com/s/oqur6k70poyscxj/azure.png?dl=1)](http://computer-management.westeurope.cloudapp.azure.com/)

###Descripción
Se trata de realizar la infraestructura virtual necesaria para levantar una aplicación web que se encargue de controlar y automatizar la tarea de administrar y controlar la entrega y recogida de equipos informáticos por la Oficina de Software Libre así como el proceso de catalogarlos adecuadamente y generar informes.

###Infraestructura

En una primera aproximación del problema, el proyecto contará con los siguientes elementos:

- Servidor web para dar servicio
- Servidores de bases de datos( Datos equipos informáticos e informes)
- Servidores Azure, Openshift o similar
- Integración continua
- Framework de alto nivel, como por ejemplo Django 
- Servicios externos

En cuanto avance más en la asignatura, es posible que añada o elimine algún elemento. 


###Inscripción en el concurso de software libre

![inscripcion](https://www.dropbox.com/s/7yrlzu2pkvbtobb/concurso.png?dl=1)

###Datos de contacto

Para cualquier cosa, contactar con [hugobarzano@gmail.com]
Twitter: @comp_mana


### Herramienta de Construcción

Para automatizar el proceso de instalación,testeo, documentación y ejecución utilizo el siguiente makefile:

	install: 
		sudo python setup.py install
	
	test: 
		python manage.py test

	doc:
		 epydoc --html ComputerManagement/
	
	run:
		sudo python manage.py runserver 0.0.0.0:80 &


### Integración Continua

Para que el proyecto cuente con integración continua he utilizado [travis](https://travis-ci.org/) por su fácil sincronización con github.
En la web de travis, debemos indicar que repositorios queremos relacionar e incluir en ellos su correspondiente .travis.yml 
![Travis](https://travis-ci.org/hugobarzano/osl-computer-management.svg?branch=master)

	language: python
	python:
 		- "2.7"

	install:
 		- sudo apt-get install python-dev
 		- pip install --upgrade pip 
 		- pip install Django 

	script:
 		- python manage.py test




### PaaS: Heroku

Para Realizar el despliegue de la aplicación en un PaaS he decidido utilizar Heroku. [Heroku](https://www.heroku.com/home) es una plataforma en la nube basado en un sistema de contenedores gestionado, con servicios de datos integrados y un potente ecosistema, para implementar y ejecutar aplicaciones modernas. He decidido utilizar Heroku debido a su fácil integración con github y por ser de carácter gratuito(al menos algunos servicios). Heroku se caracteriza por el fichero de configuración denominado **Procfile**. En dicho fichero, indicamos a Heroku que queremos arrancar una instancia web y dejar que gunicorn ejecute nuestra aplicación dentro de ella: 

	web: gunicorn ProyectoDjango.wsgi --log-file -

Otro motivo por el cual usar Heroku es por la automatización del despliegue. Heroku nos facilita un repositorio para almacenar nuestra aplicación. Podemos actualizar el contenido de dicho repositorio y desplegar la aplicación mediante: 

	git push heroku master

Esto puede automatizarse un poco más mediante snap-ci. Como podemos observar en la siguiente captura, snap-ci nos permite vincular el repositorio en el que se encuentra la aplicación y desglosar en un pipeline los distintos estados por los que pasa el despliegue, pasando por la instalación de dependencias y ejecución de los test para integración continua hasta despliegue con heroku. Snap-ci detectará los cambios con cada git push al repositorio, iniciándose el siguiente ciclo de construcción: 

![snap_ci](https://www.dropbox.com/s/ghwn1qquer0at5x/pipline.png?dl=1) 

El siguiente enlace les llevará al [despliegue](https://computer-management.herokuapp.com/)

La aplicación en local corre sobre una base de datos sqlite3 y en heroku sobre la postgresql que nos presta el PaaS al crear la aplicación.
Para que heroku coja nuestros modelos es necesario ejecutar:
	
	 heroku run python manage.py syncdb
 
La aplicación cuenta con funcionalidades para consultar, crear, modificar y eliminar dispositivos utilizando **Django REST framework**
Para testear estas funcionalidades he simulado un navegador-cliente utilizando APITestCase y RequestFactory

###Fabric: Despliegue remoto

[Fabric](http://www.fabfile.org/) es un biblioteca Python y herramienta en línea de comandos que hace uso de SSH para llevar acabo tareas de administración o despliegue de aplicaciones.
 
Mediante el uso de Fabric he creado un [fabfile.py](https://github.com/hugobarzano/osl-computer-management/blob/master/fabfile.py) en el que describo las distintas tareas de administración y despliegue que se pueden llevar a cabo de manera remota.
Puedes consultar los detalles de como he realizado el despliegue remoto [aquí](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/fabric.md) 

Para probar el entorno de manera online, he puesto a disposición del usuario una [maquina virtual azure](http://computer-management.westeurope.cloudapp.azure.com/)
Puedes consultar los detalles de como he creado y configurado la máquina azure [aquí](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/azure.md)


###Docker Hub

[Docker Hub](https://www.docker.com/docker-hub) es un servicio de registro en la nube para la construcción y envío de aplicaciones o servicios utilizando contenedores. Proporciona un recurso centralizado para la creación, distribución y la gestión de imágenes. Permite al usuario la automatización del flujo de trabajo a lo largo de la línea de desarrollo.

Para que Docker Hub automatice la constitución, es necesario crear un fichero de configuración [Dockerfile](https://github.com/hugobarzano/osl-computer-management/blob/master/Dockerfile) con todo lo necesario para que nuestra aplicación funcione. 

Pasos necesarios para [Configurar Docker Hub](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/dockerHub.md) correctamente. 

Enlace al repositorio de la [Automated Build](https://hub.docker.com/r/hugobarzano/osl-computer-management/)  

Podemos descargar el entorno mediante la orden

	sudo docker pull hugobarzano/osl-computer-management:computer-management

