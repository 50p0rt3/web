from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Home")

def service(request):
    return HttpResponse("Services")

def shop(request):
    return HttpResponse("Shop")

def blog(request):
    return HttpResponse("Blog")

def contact_us(request):
    return HttpResponse("Contact us")


