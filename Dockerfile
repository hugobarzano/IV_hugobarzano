FROM ubuntu:14.04

#Autor
MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>

#Actualizar
RUN sudo apt-get update	-y

#Instalar paquetes basicos
RUN sudo apt-get install -y build-essential
RUN sudo apt-get install -y git
RUN sudo apt-get install -y python-setuptools

#Instalar bases de datos
#RUN sudo apt-get install -y postgresql postgresql-contrib
#RUN sudo apt-get install mysql-server mysql-client
#RUN sudo apt-get install mongodb

#Descargar aplicacion
RUN sudo git clone https://github.com/hugobarzano/osl-computer-management.git

#Instalamos la aplicacion
RUN cd osl-computer-management
RUN make install

#Ejecutamos la aplicacion
RUN make run

