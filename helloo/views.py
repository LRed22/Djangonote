
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Hello")
    #Separate Html from Pyhton
    return render(request, "hello/index.html")
    
def brian(request):
    return HttpResponse("Hello, Brian")

def Love(request):
    return HttpResponse("Hello, Love!")

def David(request):
    return HttpResponse("Hello, David?")

def greet(request, name):
    # add capitalize #
   # return HttpResponse(f"Hello, {name.capitalize()}!")

    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    } )
