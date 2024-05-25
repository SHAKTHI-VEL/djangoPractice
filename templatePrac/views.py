from django.shortcuts import render
from .models import Course
# Create your views here.

def all_course(request):
    courses=Course.objects.all
    return render(request,'templatePrac/all.html',{'courses':courses})