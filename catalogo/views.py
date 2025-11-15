from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Auto

def lista_autos(request):
    autos = Auto.objects.filter(disponible=True)
    return render(request, 'catalogo/lista_autos.html', {'autos': autos})

def detalle_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'catalogo/detalle_auto.html', {'auto': auto})