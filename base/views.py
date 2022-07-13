from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm
import logging


# Create your views here.

# team_members = [
#     {'id':1, 'name':'Adrien Olczak (admin)', 'number': '415-310-619', 'email': 'adrien@instawork.com'},
#     {'id':2, 'name':'Charlene Pham', 'number': '415-310-619', 'email': 'charlene@instawork.com'},
#     {'id':3, 'name':'Benson Mach', 'number': '415-310-619', 'email': 'benson@instawork.com'},
#     {'id':4, 'name':'Dan Petrie', 'number': '415-310-619', 'email': 'dan@instawork.com'}
# ] 


def list(request):
    team_members = Member.objects.values()

    context = {'team_members': team_members}
    return render(request, 'base/list.html', context)

def add(request):
    form = MemberForm()
    if request.method == 'POST':
       # print(request.POST)
       form = MemberForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('list')
    context = {'form': form}
    return render(request, 'base/add.html', context)

def edit(request, id):
    # member = None
    # for person in team_members:
    #     if person['id'] == int(id):
    #         member = person
    member = Member.objects.get(id=id)
    form = MemberForm(instance=member)

    if request.method == 'POST':
       # print(request.POST)
       form = MemberForm(request.POST, instance=member)
       if form.is_valid():
            form.save()
            return redirect('list')


    context = {'form': form, 'member': member}
    return render(request, 'base/edit.html', context)  

def delete(request, id):
    member = Member.objects.get(id=id)
    # if request.method == 'POST':
       # print(request.POST)
    member.delete()
    return redirect('list')
    # return render(request, 'base/delete.html', {'form': member})