from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# Ejemplo de una pagina con funcion

def test(request):
    template = loader.get_template('nido/test.html')
    context = {
        'aves': ['Quetzal', 'Aguila Arpia', 'Emu', 'Colibri']
    }
    return HttpResponse(template.render(context, request))

# Ejemplo de una pagina simple

def test2(request):
    return render(request, 'nido/test2.html')