from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Curso
from persona.views import Persona    

def curso(request):
    
    cursos = Curso.objects.all();
    
    return render(request, 'curso.html', {
        'title': 'Lista de Cursos',
        'curso': cursos
    })
    


def formCreateCurso(request):
    profesores= Persona.objects.filter(rol="Profesor")
    if request.method =="POST":
        nombre = request.POST.get('Nombre_curso')
        capacidad_maxima = request.POST.get('capacidad_maxima')
        profesor = request.POST.get('profesor')
        
        curso = Curso(
            nombre=nombre,
            capacidad_maxima=capacidad_maxima,
            profesor=Persona.objects.get(id=profesor),
        )
        
        curso.save()
        
        return redirect( 'cursos')
    return render(request, 'curso_nuevo.html',{"profesores":profesores})
