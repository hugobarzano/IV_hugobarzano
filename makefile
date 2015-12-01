#Makefile

install: 
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt
	
test: 
	python manage.py test

doc:
	 epydoc --html ComputerManagement/
	
run:
	python manage.py runserver&
