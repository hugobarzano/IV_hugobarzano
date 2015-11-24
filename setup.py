from setuptools import setup

setup(name='ComputerManagement',
	version='0.0.1',
	description='Plataforma para automatizar el proceso de recogida y catalogacion de equipos informaticos',
	url='https://github.com/hugobarzano/osl-computer-management',
	author='Hugo Barzano Cruz',
	author_email='hugobarzano@gmail.com',
	license='GNU General Public License',
	packages=['ComputerManagement'],
	install_requires=[
		dj-database-url==0.3.0
		dj-static==0.0.6
		Django==1.8.5
		django-toolbelt==0.0.1
		djangorestframework==3.3.0
		foreman==0.9.7
		futures==3.0.3
		gunicorn==19.3.0
		psycopg2==2.6.1
		Pygments==2.0.2
		requests==2.8.1
		requests-futures==0.9.5
		static3==0.6.1
		wheel==0.24.0
		whitenoise==2.0.4
	],
	zip_safe=False)
