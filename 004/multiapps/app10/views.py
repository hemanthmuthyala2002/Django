from django.shortcuts import render,HttpResponse

# Create your views here.
def sampleapp10view1(request):
    return HttpResponse('<h1>HELLO YOU ARE IN VIEW-1,APP-10</h1>')
def sampleapp10view2(request):
    return HttpResponse ('hello this is view1 in app10')
