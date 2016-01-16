#Makefile

install: 
	python setup.py install
	
test: 
	python manage.py test

doc:
	 epydoc --html ComputerManagement/
	
sincronizacion: 
	sudo service postgresql start
	sudo python manage.py syncdb --noinput

run:
	sudo python manage.py runserver 0.0.0.0:80 &

docker:
	sudo service docker restart
	sudo docker build -f Dockerfile -t aplicacion --no-cache=true .
	nohup sudo docker run -t -i aplicacion sh -c "ifconfig && cd /osl-computer-management && python manage.py syncdb --noinput && sudo python manage.py runserver 0.0.0.0:80"

docker_compose:
	sudo service docker restart
	sudo docker pull postgres
	sudo docker build -f Dockerfile -t aplicacion --no-cache=true .
	nohup sudo docker-compose run web
