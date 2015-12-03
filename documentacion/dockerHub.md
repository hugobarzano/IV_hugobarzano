# Generar Automated Build con Docker Hub

Para generar una build de manera automática con [Docker Hub](https://hub.docker.com/),
lo primero que debemos hacer es registrarnos e iniciar sesión.

Una vez en nuestro perfil, debemos vincular la cuenta de github a Docker Hub y elegir el repositorio que
deseamos automatizar

![docker_hub](https://www.dropbox.com/s/70lqtckzqjmz0f7/docker_hub.png?dl=1)

Lo siguiente es configurar los disparadores de la build para que cojan la rama que deseamos automatizar

![docker_hub2](https://www.dropbox.com/s/4oa3svnpn6ody2m/docker_hub2.png?dl=1)

De aquí en adelante, la build saltará a golpe de **git push**
Podemos comprobar que efectivamente para construirla utiliza el Dockerfile  del repositorio

![docker_hub3](https://www.dropbox.com/s/kso18cybcmoxdek/docker_hub3.png?dl=1) 

Por ultimo, podemos consultar el estado de la build

![docker_hub4](https://www.dropbox.com/s/aswlbojzljnr87a/docker_hub4.png?dl=1)

Podemos obtener la imagen mediante 

	sudo docker pull hugobarzano/osl-computer-management:computer-management
