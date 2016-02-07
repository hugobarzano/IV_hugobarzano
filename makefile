#Makefile

install:
	python setup.py install

test:
	python manage.py test

doc:
	 epydoc --html ComputerManagement/

inicializar:
	sudo pip install -r requirements.txt
	python manage.py makemigrations --noinput
	python manage.py migrate --noinput
	python manage.py syncdb --noinput
	chmod +x populate.py
	python populate.py

free:
	sudo fuser -k 80/tcp

run:
	python manage.py collectstatic --noinput
	sudo python manage.py runserver 0.0.0.0:80

heroku:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	heroku login
	#heroku apps:destroy --app heroku-deploy-hugo --confirm heroku-deploy-hugo
	#heroku run echo Espera 15 segundos a liberar el nombre de dominio
	#heroku run sleep 15
	#heroku create heroku-deploy-hugo
	#heroku addons:create heroku-postgresql:hobby-dev
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku run python manage.py makemigrations --noinput
	heroku run python manage.py migrate --noinput
	heroku run python manage.py syncdb --noinput
	heroku run python manage.py collectstatic --noinput
	heroku run chmod +x populate.py
	heroku run python populate.py
	heroku ps:scale web=1
	heroku open

install_docker:
	sudo -i apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-key$
	sudo -i echo /etc/apt/sources.list.d/docker.list deb https://apt.dockerproject.$
	sudo -i apt-get update
	#sudo -i apt-cache policy docker-engine
	#sudo -i apt-get -y install linux-image-extra-$(uname -r)
	#sudo -i apt-get -y install linux-image-generic-lts-trusty
	sudo -i apt-get -y install curl
	curl -sSL https://get.docker.com/gpg | sudo apt-key add -
	curl -sSL https://get.docker.com/ | sh
	sudo -i apt-get -y install python-pip
	sudo -i pip install docker-compose

	python manage.py makemigrations --noinput
	python manage.py migrate --noinput

docker:
	sudo service docker restart
	sudo docker build -f Dockerfile -t aplicacion --no-cache=true .
	sudo docker run -t -i aplicacion sh -c "ifconfig && cd /osl-computer-management &&  python manage.py makemigrations --noinput && 	python manage.py migrate --noinput && python manage.py syncdb --noinput && python populate.py && sudo python manage.py runserver 0.0.0.0:80"

docker_compose:
	sudo service docker restart
	sudo docker pull postgres
	sudo docker pull hugobarzano/osl-computer-management:computer-management
	sudo docker-compose up
	echo Voy a esperar 10 segundos a la base de datos
	sleep 10
	sudo docker-compose run web

install_vagrant:
	sudo -i apt-get update
	sudo apt-get install -y virtualbox virtualbox-dkms
	sudo apt-get install -y vagrant
	vagrant plugin install vagrant-azure

docker_deploy:
	cd vagrantDocker/ && vagrant up --provider=azure

docker_provision:
	cd vagrantDocker/ && vagrant provision

ansible_deploy:
	cd vagrantSimple/ && vagrant up --provider=azure

ansible_provision:
	cd vagrantSimple/ && vagrant provision
