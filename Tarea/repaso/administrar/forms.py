from django import forms
from .models import Alumno
from .models import Materia


class FormularioAlu(forms.ModelForm):
	class Meta:
	   		model=Alumno
	   		fields=["nombres","apellidos","cedula","genero"]
	
class FormularioMat(forms.ModelForm):
	class Meta:
			model=Materia
			fields=["nombre","creditos","cupos"]
