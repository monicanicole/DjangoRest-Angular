from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$','administrar.views.listar'),
    url(r'^crear/$', 'administrar.views.crear'),
    url(r'^crearm/$', 'administrar.views.crearm'),
    url(r'^modificar/$', 'administrar.views.modificar'),
    url(r'^modificarm/$', 'administrar.views.modificarm'),
    url(r'^eliminar/$', 'administrar.views.eliminar'),
    url(r'^eliminarAlumno/$', 'administrar.views.eliminarAlumno'),
    url(r'^eliminarm/$', 'administrar.views.eliminarm'),
    url(r'^eliminarMateria/$', 'administrar.views.eliminarMateria'),
  

]