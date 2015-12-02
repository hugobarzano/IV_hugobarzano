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
		'dj-database-url',
		'dj-static',
		'Django',
		'django-toolbelt'
		'djangorestframework',
		'foreman',
		'futures',
		'gunicorn',
		'Pygments',
		'static3',
		'wheel',
		'whitenoise',
	],
	zip_safe=False)
