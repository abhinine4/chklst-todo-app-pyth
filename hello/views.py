from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def myView(request):
    return HttpResponse('Hello, Beautiful World!')