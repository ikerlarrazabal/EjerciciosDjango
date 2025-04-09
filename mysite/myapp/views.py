from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Empresa
#devuelve el listado de empresas
def index(request):
 empresas = Empresa.objects.order_by('nombre')
 output = ', '.join([e.nombre for e in empresas])
 return HttpResponse(output)