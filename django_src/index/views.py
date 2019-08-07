from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Mindslab. 2nd_LinuxStudy Best Company GM")