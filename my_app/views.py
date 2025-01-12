from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def about(request):
    return HttpResponse("About Me")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def add(request, num1, num2):

    return HttpResponse(f"the total is {num1 + num2}")
