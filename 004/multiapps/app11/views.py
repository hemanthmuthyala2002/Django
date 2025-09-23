from django.shortcuts import render,HttpResponse

# Create your views here.
def sampleapp11view1(request):
    return HttpResponse('<h1>HELLO YOU ARE IN VIEW-1,APP-11</h1>')

