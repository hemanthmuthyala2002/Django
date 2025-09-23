from django.shortcuts import render,HttpResponse

# Create your views here.
def sample_view1(request):
    return HttpResponse('<b> this is view1 in feeApp</b>')
def sample_view2(request):
    return HttpResponse('<b> this is view2 in feeApp</b>')
