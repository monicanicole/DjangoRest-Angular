from rest_framework import serializers
from administrar.models import Alumno
from administrar.models import Materia


class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumno
		fields=('nombres','apellidos','cedula','genero')

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=('nombre','creditos','cupos')
