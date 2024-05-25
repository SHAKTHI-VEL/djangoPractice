from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to django home server")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Welcome to django about server")
    