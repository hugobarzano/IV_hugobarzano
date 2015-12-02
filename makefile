#Makefile

install: 
	python setup.py install
	
test: 
	python manage.py test

doc:
	 epydoc --html ComputerManagement/
	
run:
	python manage.py runserver&
