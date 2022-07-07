from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

team_members = [
    {'id':1, 'name':'Adrien Olczak (admin)', 'number': '415-310-619', 'email': 'adrien@instawork.com'},
    {'id':2, 'name':'Charlene Pham', 'number': '415-310-619', 'email': 'charlene@instawork.com'},
    {'id':3, 'name':'Benson Mach', 'number': '415-310-619', 'email': 'benson@instawork.com'},
    {'id':4, 'name':'Dan Petrie', 'number': '415-310-619', 'email': 'dan@instawork.com'}
]



def list(request):
    context = {'team_members': team_members}
    return render(request, 'base/list.html', context)

def add(request):
    return render(request, 'base/add.html')

def edit(request, id):
    return render(request, 'base/edit.html') 