from administrar.models import Alumno
from administrar.models import Materia

from .serializable import AlumnoSerializable
from .serializable import MateriaSerializable


from rest_framework import viewsets 

class AlumnoViewSet(viewsets.ModelViewSet): #herencia
	#llamo al objeto serializable
	serializer_class=AlumnoSerializable
	#defino la consulta de datos que se enviaran en ws
	queryset=Alumno.objects.all().order_by('apellidos')

class MateriaViewSet(viewsets.ModelViewSet): #herencia
	#llamo al objeto serializable
	serializer_class=MateriaSerializable
	#defino la consulta de datos que se enviaran en ws
	queryset=Materia.objects.filter(cupos__lte=29)

