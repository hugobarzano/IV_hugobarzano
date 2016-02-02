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
	sudo python manage.py runserver 0.0.0.0:80

heroku:
	wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	heroku login
	heroku create
	heroku addons:create heroku-postgresql:hobby-dev
	git add .
	git commit -m "despliegue en heroku"
	git push heroku master
	heroku run python manage.py makemigrations --noinput
	heroku run python manage.py migrate --noinput
	heroku run python manage.py syncdb --noinput
	heroku ps:scale web=1
	heroku open

docker:
	sudo service docker restart
	sudo docker build -f Dockerfile -t aplicacion --no-cache=true .
	sudo docker run -t -i aplicacion sh -c "ifconfig && cd /osl-computer-management && python manage.py syncdb --noinput && sudo python manage.py runserver 0.0.0.0:80"

docker_compose:
	sudo service docker restart
	sudo docker pull postgres
	sudo docker build -f Dockerfile -t aplicacion --no-cache=true .
	nohup sudo docker-compose run web
