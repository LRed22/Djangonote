
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello")
    
def brian(request):
    return HttpResponse("Hello, Brian")

def Love(request):
    return HttpResponse("Hello, Love!")

def David(request):
    return HttpResponse("Hello, David?")

def greet(request, name):
    # add capitalize #
    return HttpResponse(f"Hello, {name.capitalize()}!")

    
