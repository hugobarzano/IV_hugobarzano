# OSL Computer Management

##Proyecto para Infraestructura Virtual 2015/2016
[![Build Status](https://travis-ci.org/hugobarzano/osl-computer-management.svg?branch=master)](https://travis-ci.org/hugobarzano/osl-computer-management) [![Build Status](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master/build_image)](https://snap-ci.com/hugobarzano/osl-computer-management/branch/master)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://computer-management.herokuapp.com/)
[![Azure](https://www.dropbox.com/s/oqur6k70poyscxj/azure.png?dl=1)](http://computermanagementansible.cloudapp.net/)
[![Azure2](https://www.dropbox.com/s/v50imf9aqkxvhgr/docker-machine-azure.png?dl=1)](http://computermanagementdocker.cloudapp.net/)



###Descripción
Se trata de realizar la infraestructura virtual necesaria para levantar una aplicación web que se encargue de controlar y automatizar la tarea de administrar y controlar la entrega y recogida de equipos informáticos por la Oficina de Software Libre así como el proceso de catalogarlos adecuadamente y generar informes.

###Infraestructura

El proyecto cuenta con la siguiente infraestructura:

- Framework de alto nivel Django
- Sqlite3 y PostgreSQL como motores de bases de datos
- Integración continua
- Heroku como Platform as a Service
- Azure como Infrastructure as a service
- Servicios externos como Easy Maps

###Inscripción en el concurso de software libre

![inscripcion](https://www.dropbox.com/s/7yrlzu2pkvbtobb/concurso.png?dl=1)

###Datos de contacto

Para cualquier cosa, contactar con [hugobarzano@gmail.com]
Twitter: @comp_mana


### Herramienta de Construcción

Para automatizar las funcionalidades de la infraestructura utilizo este [makefile](https://github.com/hugobarzano/osl-computer-management/blob/master/makefile). Es capaz de:

####Trabajando en local
	make install: instala todo lo necesario para ejecucion local
	make install_docker: instala docker y docker-compose
	make install_vagrant: instala vagrant, virtual box y plugins para vagrant

	make inicializar: Crea la base de datos y las sincroniza
	make run: ejecuta la aplicacion
	make docker: Genera una imagen funcional utilizando un dockerfile y la arranca
	make docker_compose: Utiliza imagenes funcionales para componer servicios y arrancarlos

	make doc: Genera la documentacion
	make free: libera el puerto 80, matando cualquier proceso que lo use


####Trabajando en la nube
	make heroku: despliega la aplicacion en un PaaS

	make ansible_deploy: despliega la aplicacion en un IaaS
	make ansible_provision: Aprovisiona la aplicacion en el IaaS
	make ansible_destroy: Destrulle el despliegue mediante playbooks

	make docker_deploy: despliega la aplicacion en un IaaS mediante contenedores
	make docker_provision: aprovisiona la aplicacion en el IaaS mediante contenedores
	make docker_destroy: Destrulle el despliegue mediante contenedores



###Integración continua: Travis

El proceso de integración continua tiene como objetivo principal comprobar que cada actualización del código fuente no genere problemas en una aplicación que se está desarrollando.

Para que el proyecto cuente con integración continua he utilizado [travis](https://travis-ci.org/) por su fácil sincronización con github.
En la web de travis, debemos indicar que repositorios queremos relacionar e incluir en ellos su correspondiente [.travis.yml](https://github.com/hugobarzano/osl-computer-management/blob/master/.travis.yml)


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
Para testear estas funcionalidades he simulado un navegador-cliente utilizando APITestCase y RequestFactory.
Podemos realizar el despliege en heroku de manera automática mediante:

	make heroku

###Fabric: Despliegue remoto

[Fabric](http://www.fabfile.org/) es un biblioteca Python y herramienta en línea de comandos que hace uso de SSH para llevar acabo tareas de administración o despliegue de aplicaciones.

Mediante el uso de Fabric he creado un [fabfile.py](https://github.com/hugobarzano/osl-computer-management/blob/master/fabfile.py) en el que describo las distintas tareas de administración y despliegue que se pueden llevar a cabo de manera remota.
Puedes consultar los detalles de como he realizado el despliegue remoto [aquí](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/fabric.md)

Para probar el depliegue rentorno utilizando fabric, es necesarios disponer de una maquina virtual virgen.
Puedes consultar los detalles de como crear y configurar máquinas azure desde el portal de administración [aquí](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/azure.md)


###Docker Hub

[Docker Hub](https://www.docker.com/docker-hub) es un servicio de registro en la nube para la construcción y envío de aplicaciones o servicios utilizando contenedores. Proporciona un recurso centralizado para la creación, distribución y la gestión de imágenes. Permite al usuario la automatización del flujo de trabajo a lo largo de la línea de desarrollo.

Para que Docker Hub automatice la constitución, es necesario crear un fichero de configuración [Dockerfile](https://github.com/hugobarzano/osl-computer-management/blob/master/Dockerfile) con todo lo necesario para que nuestra aplicación funcione.

Pasos necesarios para [Configurar Docker Hub](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/dockerHub.md) correctamente.

Enlace al repositorio de la [Automated Build](https://hub.docker.com/r/hugobarzano/osl-computer-management/)

Podemos descargar el entorno mediante la orden

	sudo docker pull hugobarzano/osl-computer-management:computer-management

###Trabajando con Docker

Para trabajar con docker en nuestro equipo, es necesario ejecutar el scrip de instalación como súper usuario

	sudo su
	chmod +x install_docker.sh
	./install_docker.sh

El entorno almacenado en Docker hub es una imagen básica pre-construida utilizando el servicio sqlite3.
Para trabajar con este entorno podemos utilizar la herramienta de construcción makefile

	make docker

Si queremos trabajar con algo mas potente, podemos utilizar la composición de servicios (docker-compose) y orquestar la aplicación con algún motor de bases de datos como por ejemplo PostgreSQL. Para trabajar con este entorno podemos utilizar la herramienta de construcción makefile

	make docker_compose


### Ansible

Ansible es una herramienta de automatización que permite configurar sistemas, implementar software y orquestar tareas complejas como por ejemplo despliegues continuos. He decidido utilizar ansible por su fiabilidad, facilidad de uso y seguridad. Para poder trabajar con ansible es necesario crear un archivo de aprovisionamiento.yml en el que detallar todas las dependencias, servicios y tareas que nuestra aplicación necesita para funcionar. Aunque puede usarse de manera independiente, si la combinamos con herramientas de creación y administración de entornos vistuales como por ejemplo Vagrant, podemos llegar a consegir grandes resultados.

####Playbook para aprovisionamiento de contenedores

El primer playbook que he creado para la aplicación se puede consultar [aqui](https://github.com/hugobarzano/osl-computer-management/blob/master/vagrantDocker/playbook.yml). Este playbook actualiza el sistema base, instala dependencias, instala docker, instala la extensión docker-compose, descarga contenedores funcionales y los ejecuta. El vagrantfile asociado es [este](https://github.com/hugobarzano/osl-computer-management/blob/master/vagrantDocker/Vagrantfile)
Para realizar este tipo de despliegue solo hay que ejecutar:

		make docker_deploy

Si realizamos algun cambio en los contenedores o en los fuentes de la aplicación, podemos aprovisionarlos mediante

	make docker_provision

Si queremos destruir el despliegue de contenedores podmeos hacerlo mediante

	make docker_destroy

####Playbook para aprovisionamiento de aplicacion

El segundo playbook con el que cuenta la aplicacion se puede consultar [aqui](https://github.com/hugobarzano/osl-computer-management/blob/master/vagrantSimple/playbook.yml). Este playbook, actualizar sistema base, instala git, instala Python, incroniza la base de datos y ejecuta la aplicacion. El vagrantfile asociado es [este](https://github.com/hugobarzano/osl-computer-management/blob/master/vagrantSimple/Vagrantfile)
Para realizar este tipo de despliegue solo hay que ejecutar:

		make ansible_deploy

Si realizamos algun cambio sobre los fuentes de la aplicacion podemos aprovisionarla mediante

	make ansible_provision

Si queremos destruir el despliegue podemos hacerlo mediante

	make ansible_destroy


#Vagrant

Vagrant es una herramienta open-source para la creación y configuración de entornos de desarrollo virtualizados.
Vagrant proporciona entornos de trabajo fáciles de configurar, reproducibles y portátiles. Está desarrollado con Ruby y utiliza  el sistema  de virtualización Virtualbox de Oracle. Este proyecto tiene asociado un fichero denominado Vagrantfile cuya función principal es la de  describir el tipo de máquinas necesarias para la aplicación, cómo configurarlas y como provisionarlas. Los despliegues del punto anterior utilizan este Vagrantfile()

Dependiendo del provedor de servicio, vagrant será configurado de una manera u otra. En mi caso, voy a utilizar azure, por lo que vagrant
necesita el plugin Microsoft Azure provider to Vagrant. Con este plugin detallamos entre otras cosas nuestras credenciales en azure. Podemos consultar como configurar las credenciales [aqui](https://github.com/hugobarzano/osl-computer-management/blob/master/documentacion/credenciales.md)

Con vagrant no solo podemos trabajar individualmente maquina a máquina, podemos utilizar vagrant-multimachine para crear en paralelo dos maquinas virtuales y aprovisionarlas cada una como quereamos. Puede consular el vagrantfile para la creación y aprovisionamiento de dos maquinas independientes aqui[]()

Si deseamos aprender mas sobre Vagrant, podemos consultar este [documento](https://www.dropbox.com/s/ann1va5bqrgetvv/Vagrant.pdf?dl=1)
