
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello")
    
def brian(request):
    return HttpResponse("Greetings, Brian")

def Love(request):
    return HttpResponse("hello, Love!")

def David(request):
    return HttpResponse("What's up David?")
