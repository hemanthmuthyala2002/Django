from django.shortcuts import render

# Create your views here.
def staicimage(request):
    return render(request,"myapp/staticimage.html")
