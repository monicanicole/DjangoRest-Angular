from django.contrib import admin
from .models import Alumno
from .models import Materia

class AdminAlumno(admin.ModelAdmin):
	list_display=["__str__","nombres","apellidos","cedula","genero"]
	class Meta:
		model=Alumno

admin.site.register(Alumno,AdminAlumno)

class AdminMateria(admin.ModelAdmin):
	list_display=["__str__","nombre","creditos","cupos"]
	class Meta:
		model=Materia
admin.site.register(Materia,AdminMateria)
