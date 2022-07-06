from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list(request):
    return HttpResponse('List page')

def add(request):
    return HttpResponse('Add page')

def edit(request):
    return HttpResponse('Edit page') 