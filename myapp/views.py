
from django.shortcuts import render, redirect
from .forms import ProgramaForm

def crear_programa(request):
    if request.method == 'POST':
        formulario = ProgramaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crear_programa')
    else:
        formulario = ProgramaForm()

    return render(request, 'myapp/crear_programa.html', {
        'formulario': formulario
    })
