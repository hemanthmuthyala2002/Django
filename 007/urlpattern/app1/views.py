from django.shortcuts import render,HttpResponse

def sample_name(request,name):
    return HttpResponse(name)
