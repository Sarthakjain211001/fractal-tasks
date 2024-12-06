from django.http import HttpResponse
from .models import PersonModel
from .forms import PersonForm
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Welcome to Django app sarthak !!!")

def create_view(request):
    context = {}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'create_view.html', context)