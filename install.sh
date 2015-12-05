#!/bin/bash

#Actualizar Sistema Base
echo "actualizar sistema base"
sudo apt-get -y update

# Instalar Python y PostgreSQL
echo "Instalar dependencias"
sudo apt-get install -y python-setuptools
sudo apt-get -y install python-dev
sudo apt-get -y install build-essential
sudo apt-get -y install python-psycopg2
sudo apt-get -y install libpq-dev
sudo easy_install pip
sudo pip install --upgrade pip

#Instalamos la aplicacion
echo "instalar requirements"
cat requirements.txt
sudo pip install -r requirements.txt

