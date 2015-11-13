# OSL Computer Management

##Proyecto para Infraestructura Virtual 2015/2016
![Travis](https://travis-ci.org/hugobarzano/osl-computer-management.svg?branch=master) [![Build Status](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master/build_image)](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master)
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


## - Segundo Hito - 

En una segunda aproximación al problema, la aplicación cuenta con dos modelos (Dispositivo e Informe) sobre los que se ejecutan una serie de test. Los test se encuentran en el archivo test.py que genera el framework Django al comenzar una aplicación. Para automatizar el proceso de generar documentación utilizo epydoc.

### Herramienta de Construcción

Para automatizar el proceso de instalación,testeo, documentación y ejecución utilizo el siguiente makefile:

	install: 
		sudo python setup.py install
	
	test: 
		python manage.py test

	doc:
		 epydoc --html ComputerManagement/
	
	run:
		python manage.py runserver

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




