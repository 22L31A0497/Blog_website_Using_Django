from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("This is the first project")

def demo(request):
    return HttpResponse("This is demo another function")



def home(request):
    return render(request, 'index.html')

def jagan(request):
    return render(request,'base.html',{"name":"jagan","age":"21"})

def index(request):
    return render(request, 'index.html')