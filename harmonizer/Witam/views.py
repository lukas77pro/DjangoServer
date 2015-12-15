from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello");


def elo(request):
    return HttpResponse("Elo");

# Create your views here.
