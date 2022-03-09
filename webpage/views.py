from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("About")

# Create your views here.
