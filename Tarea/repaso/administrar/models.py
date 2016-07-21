from django.db import models
class Alumno(models.Model):

	listaGenero=(
		('f','femenino'),
		('m','masculino'),

	)

	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	cedula=models.CharField(max_length=10)
	genero=models.CharField(max_length=10,choices=listaGenero)
	
	def __str__(self):
		return self.cedula

class Materia(models.Model):

	nombre= models.CharField(max_length=50)
	creditos= models.CharField(max_length=50)
	cupos=models.CharField(max_length=60)

	def __str__(self):
		return self.nombre
