##Creación de credenciales para Vagrant

Partiendo de que tenemos instalado vagrant y azure-cli , lo primero que tenemos que hacer es instalar es el provisionador azure para vagrant

	vagrant plugin install vagrant-azure

![imagen](https://www.dropbox.com/s/z8pwe08h8npu79o/va.png?dl=1)

Para poder toquetear las maquinas azure, tendremos que descargar el archivo de Configuración de publicación, que contiene credenciales seguras e información adicional acerca de nuestra suscripción Azure

	azure login
	azure account download

Debemos de abrir el enlace y descargar el archivo

![imagen](https://www.dropbox.com/s/4wrainq0e9w9aid/va2.png?dl=1)

Una vez que lo tengamos, debemos importarlo

	 azure account import Pase\ para\ Azure-1-8-2016-credentials.publishsettings

Lo siguiente es obtener archivos PEM con las claves públicas y privadas, y los certificados X509

	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/.ssh/azurevagrant.key -out ~/.ssh/azurevagrant.key
	chmod 600 ~/.ssh/azurevagrant.key
	openssl x509 -inform pem -in ~/.ssh/azurevagrant.key -outform der -out ~/.ssh/azurevagrant.cer

Una vez creados, es necesario subir el certificado.cer al portal de azure

![imagen](https://www.dropbox.com/s/nwjahryrdqu5506/va3.png?dl=1)

Para autenticar la maquina azure desde el Vagrantfile, necesitamos un archivo.pem. Para generarlo necesitamos hacer un truco, primero ejecutar

	openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem

para generarlo y después concatenarle el fichero.key. Esto es necesario para que el fichero.pem contenga tanto la clave publica como la privada.

	cat azurevagrant.key > azurevagrant.pem

###Nota: Es necesario que las llaves y certificados se llamen azurevagrant.* o los scripts de despliegue fallarán.  
