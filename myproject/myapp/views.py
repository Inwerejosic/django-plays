from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Ogechi',
        'age': 30,
        'nationality': 'Nigerian'
    }
    return render(request, 'index.html', context)
