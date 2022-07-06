from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    return render(request, 'list.html')

def add(request):
    return render(request, 'add.html')

def edit(request):
    return render(request, 'edit.html') 