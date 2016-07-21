from django.shortcuts import render
from django.shortcuts import redirect

from .forms import FormularioAlu
from .forms import FormularioMat
from .models import Alumno
from .models import Materia
from django.contrib import messages



def listar(request):
	alumnos=Alumno.objects.all()
	materia=Materia.objects.all()
	context={
		'alumnos':alumnos,
		'materia':materia,
	}

	return render(request,"listar.html",context)

def crear(request):
	
	f=FormularioAlu(request.POST or None)

	if request.method=="POST":
		if f.is_valid():
			f_data=f.cleaned_data

			c=Alumno()
			c.nombres=f_data.get("nombres")
			c.apellidos=f_data.get("apellidos")
			c.cedula=f_data.get("cedula")
			
			c.sexo=f_data.get("sexo")
			
			if (c.save()!=True):
				return redirect(listar)
	context={
		'f':f,
		
	}
	return render(request,"crear.html",context)
def crearm(request):
	m=FormularioMat(request.POST or None)
	if  request.method=="POST":
		if m.is_valid():
			m_data=m.cleaned_data

			s=Materia()
			s.nombre=m_data.get("nombre")
			s.creditos=m_data.get("creditos")
			s.cupos=m_data.get("cupos")
			if (s.save()!=True):
				return redirect(listar)
	context={
		'm':m
	}
	return render(request,"crearm.html",context)


def modificar(request):
	alumno=Alumno.objects.get(cedula=request.GET['cedula'])
	f=FormularioAlu(request.POST or None)
	f.fields["nombres"].initial=alumno.nombres
	f.fields["apellidos"].initial=alumno.apellidos
	f.fields["cedula"].initial=alumno.cedula
	f.fields["genero"].initial=alumno.genero
	

	if f.is_valid(): #almacenar el valor nuevo
		f_data=f.cleaned_data
		alumno.nombres=f_data.get("nombres")
		alumno.apellidos=f_data.get("apellidos")

		alumno.save()
		return redirect(listar)

	
	context={
		'form':f,
		'alumno':alumno,
		
	}
	return render(request,"modificar.html",context)

def modificarm(request):
	
	materia=Materia.objects.get(nombre=request.GET['nombre'])
	m=FormularioMat(request.POST or None)
	m.fields["nombre"].initial=materia.nombre
	m.fields["creditos"].initial=materia.creditos
	m.fields["cupos"].initial=materia.cupos
	
	

	if m.is_valid(): #almacenar el valor nuevo
		m_data=m.cleaned_data
		materia.nombre=m_data.get("nombre")
		materia.creditos=m_data.get("creditos")
		materia.cupos=m_data.get("cupos")
		materia.save()
		return redirect(listar)

	context={
		'formm':m,
		'materia':materia,
	}
	return render(request,"modificarm.html",context)


def eliminar(request):
	alumno=Alumno.objects.get(cedula=request.GET['cedula'])
	context={
		'alumno':alumno,
		
	}
	return render(request,"eliminar.html",context)

def eliminarAlumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el cliente", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el cliente", fail_silently=True)

	return redirect(listar)
def eliminarm (request):
	materia=Materia.objects.get(nombre=request.GET['nombre'])
	context={
		'materia':materia,
	}
	return render(request,"eliminarm.html",context)


def eliminarMateria(request):
	materia=Materia.objects.get(nombre=request.GET['nombre'])
	if materia.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el cliente", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el cliente", fail_silently=True)

	return redirect(listar)


