from django.shortcuts import render,redirect
from .models import EstudiantesCursos
from curso.models import Curso
from persona.models import Persona 

def estudianteCurso(request):
    
    estudianteCurso = EstudiantesCursos.objects.all();
    
    return render(request, 'estudiante_curso.html', {
        'title': 'Inscripcion Estudiantes',
        'estudiantes_cursos': estudianteCurso
    })

def formCreateInscripcion(request):
    estudiantes = Persona.objects.filter(rol="Estudiante")
    if request.method =="POST":

        estudiante = request.POST.get('estudiante')
        curso =request.POST.get('curso')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_final= request.POST.get('fecha_final')
        estado= request.POST.get('estado')
        nota_final= request.POST.get('nota_final')    

        estudianteCurso = EstudiantesCursos(
            estado=estado,
            fecha_inicio=fecha_inicio,
            estudiante=Persona.objects.get(id=estudiante),
            curso=Curso.objects.get(id=curso),
            fecha_final=fecha_final,
            nota_final=nota_final,
        )
        
        estudianteCurso.save()
        
        return redirect('estudiante-curso')
    return render(request, 'form-create-inscripcion.html',{'estudiantes': estudiantes,'cursos':Curso.objects.all()})