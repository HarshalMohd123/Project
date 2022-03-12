from django.shortcuts import render
from django.http import HttpResponse

def AppC(request):
    return HttpResponse('heloo')

def function(request):
    return render(request,'python.html')

def function1(request):
    return render(request,'facebook login page.html')

def function2(request):
    return render(request,'sample.html')