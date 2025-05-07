from django.shortcuts import render
from .models import Red

def index(request):
    redes = Red.objects.all()
    context = {'redes': redes}
    return render(request, 'myapp/index.html', context)
