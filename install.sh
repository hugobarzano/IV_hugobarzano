#!/bin/bash
#Autor
#MAINTAINER Hugo Barzano Cruz <hugobarzano@gmail.com>

#Actualizar Sistema Base
sudo apt-get -y update

#Descargar aplicacion
sudo apt-get install -y git
sudo git clone https://github.com/hugobarzano/osl-computer-management.git

# Instalar Python y PostgreSQL
sudo apt-get install -y python-setuptools
sudo apt-get -y install python-dev
sudo apt-get -y install build-essential
sudo apt-get -y install python-psycopg2
sudo apt-get -y install libpq-dev
sudo easy_install pip
sudo pip install --upgrade pip

#Instalamos la aplicacion
ls
cd osl-computer-management/ && ls -l
cd osl-computer-management/ && cat requirements.txt
cd osl-computer-management/ && sudo pip install -r requirements.txt

#Realizamos migraciones
cd osl-computer-management/ && python manage.py syncdb --noinput

#Ejecucion
cd osl-computer-management/ && make run
