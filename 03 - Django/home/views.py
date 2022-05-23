from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the django application")

def team(request):
    return HttpResponse("This is our team")    