from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def homepage(request):
    return HttpResponse("Home Page")


def greetings(request):
    return HttpResponse("Hello")

