from django.shortcuts import render
from .models import Tipo, Auto

# Create your views here.
def Home(request):
    return render(request, 'vistas/home.html')

def Listado(request):
    listado = Auto.objects.all()
    return render(request, 'vistas/listado.html',{'listado':listado})

def Formulario(request):
    lt = Tipo.objects.all()
    if request.POST:
        patente = request.POST["patente"]
        dueno = request.POST["dueno"]
        marca = request.POST["marca"]
        modelo = request.POST["modelo"]
        ano = request.POST["ano"]
        tipo = request.POST["tipo"]

        obj_tipo = Tipo.objects.get(id=tipo)

        auto = Auto(
            patente = patente,
            dueno = dueno,
            marca = marca,
            modelo = modelo,
            ano = int(ano),
            tipo = obj_tipo,
        )
        auto.save()
        return render(request, 'vistas/formulario_ingreso.html', {'tipos' :lt, 'mensaje':'Grabado'})
    return render(request, 'vistas/formulario_ingreso.html', {'tipos' :lt})