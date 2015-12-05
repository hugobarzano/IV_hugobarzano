from fabric.api import run, local, hosts, cd
from fabric.contrib import django


def host_type():
    run('uname -s')

def peticion():
	run('curl http://localhost:1111/')

def instalacion():
	run('cd osl-computer-management/ && sudo sh install.sh')

def sincronizacion():
	run('cd osl-computer-management/ && python manage.py syncdb --noinput')
