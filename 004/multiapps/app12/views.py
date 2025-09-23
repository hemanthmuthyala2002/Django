from django.shortcuts import render,HttpResponse

# Create your views here.
def sampleapp12view1(request):
    return HttpResponse('<h1>HELLO YOU ARE IN VIEW-1,APP-12</h1>')

