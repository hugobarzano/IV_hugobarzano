from django.conf.urls import url
from ComputerManagement import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^Dispositivos/$', views.Dispositivo_lista),
    url(r'^add_dispositivo/$', views.add_dispositivo, name='add_dispositivo'),
    url(r'^dispositivo/(?P<pk>[0-9]+)/$', views.Dispositivo_detalle),
    url(r'^dispositivo/(?P<nombre_slug>[\w\-]+)/$', views.dispositivo, name='dispositivo'),
]
