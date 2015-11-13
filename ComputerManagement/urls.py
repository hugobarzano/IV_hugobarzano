from django.conf.urls import url
from ComputerManagement import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
]
