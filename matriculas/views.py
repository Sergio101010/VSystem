from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse 
from .models import Matriculas
from persona.models import Persona 
from curso.models import Curso
from estudiantes_cursos.models import EstudiantesCursos

def matriculas(request):
    
    matriculas = Matriculas.objects.all()
    
    return render(request, 'matriculas.html', {
        'title': 'Lista de matriculas',
        'matriculas': matriculas
    })
    
def formCreateMatricula(request):
    estudiantes = Persona.objects.filter(rol="Estudiante")
    if request.method =="POST":

        estado = request.POST.get('estado')
        fecha_inicio = request.POST.get('fecha_inicio')
        costo = request.POST.get('costo')
        estudiante_curso= EstudiantesCursos.objects.get(id=request.POST.get('estudiante_curso'))

        matriculas = Matriculas(
            estado=estado,
            fecha_inicio=fecha_inicio,
            costo=costo,
            estudiante_curso=estudiante_curso,
        )
        
        matriculas.save()
        
        return redirect('matriculas')
    return render(request, 'form-create-matricula.html',{'estudiantes_cursos':EstudiantesCursos.objects.all()})

