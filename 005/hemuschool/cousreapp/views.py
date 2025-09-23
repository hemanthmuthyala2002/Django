from django.shortcuts import render,HttpResponse

# Create your views here.
def sample_view1(request):
    return HttpResponse('<b>this is view1 in cousreapp</b>')