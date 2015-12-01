FROM ubuntu:latest

#Autor
MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>

#Instalar Python con todas las dependencias

RUN apt-get update
RUN apt-get -y install python python-setuptools 
RUN apt-get install -y python-setuptools
RUN easy_install pip
	

#Descargar aplicacion
RUN apt-get install -y git
RUN sudo git clone https://github.com/hugobarzano/osl-computer-management.git

#Instalamos la aplicacion
RUN cd osl-computer-management
RUN make install

#Ejecutamos la aplicacion
RUN make run
