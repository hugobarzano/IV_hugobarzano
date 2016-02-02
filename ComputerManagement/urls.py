from django.conf.urls import url
from ComputerManagement import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^Dispositivos/$', views.Dispositivo_lista),
    url(r'^computermanagement/add_dispositivo/$', views.add_dispositivo, name='add_dispositivo'),
    #url(r'^dispositivo/(?P<pk>[0-9]+)/$', views.Dispositivo_detalle),
    #url(r'^dispositivo/(?P<bar_nombre_slug>[\w\-]+)/$', views.bar, name='bar'),
    url(r'^computermanagement/add_recogida/$', views.add_recogida, name='add_recogida'),
    url(r'^dispositivo/(?P<nombre_slug>[\w\-]+)/$', views.dispositivo, name='dispositivo'),
    url(r'^recogida/(?P<dni_donante>[\w\-]+)/$', views.recogida, name='recogida'),  # New!
    #url(r'^dispositivo/(?P<nombre_slug>[\w\-]+)/solicitarDonacion/$', views.solicitarDonacion, name='solicitarDonacion'),  # New!
    url(r'^dispositivo/(?P<nombre_slug>[\w\-]+)/solicitarDonacion/$', views.solicitarDonacion, name='solicitarDonacion'),
]
