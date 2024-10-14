from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes= Persona.objects.filter(rol='Estudiante');
    #seles * from persona
    
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

def get_profesores(request):
    
    profesores= Persona.objects.filter(rol='Profesor');
    #seles * from persona
    
    return render(request, 'lista-profesores.html', {
        'title': 'Lista de Profesores',
        'profesores': profesores
    })

def formCreateProfesor(request):
    if request.method =="POST":
        nombre = request.POST.get('nameTextInput')
        apellidos = request.POST.get('lastNameTextInput')
        dni = request.POST.get('dniTextInput')
        telefono = request.POST.get('telTextInput')
        email = request.POST.get('inputEmail')
        fecha_nacimiento = request.POST.get('birthdateInput')
        
        persona = Persona(
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            telefono=telefono,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            rol='Profesor'
        )
        
        persona.save()
        
        return redirect('lista-profesores')
    return render(request,'form-create-profesor.html')


def formCreateEstudiante(request):
    if request.method =="POST":
        nombre = request.POST.get('nameTextInput')
        apellidos = request.POST.get('lastNameTextInput')
        dni = request.POST.get('dniTextInput')
        telefono = request.POST.get('telTextInput')
        email = request.POST.get('inputEmail')
        fecha_nacimiento = request.POST.get('birthdateInput')
        
        persona = Persona(
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            telefono=telefono,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            rol='Estudiante'
        )
        
        persona.save()
        
        return redirect('lista-estudiantes')
    return render(request,'form-create-persona.html')
        
