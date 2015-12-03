#Makefile

install: 
	python setup.py install
	
test: 
	python manage.py test

doc:
	 epydoc --html ComputerManagement/
	
run:
	python manage.py runserver 0.0.0.0:1111 &
