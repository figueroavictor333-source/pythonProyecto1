from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación Django"}
    return render(request, "myapp/index.html", context)

from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myApp/estudiantes_list.html', {'estudiantes': estudiantes})


def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myApp/estudiante_detail.html', {'estudiante': estudiante})

