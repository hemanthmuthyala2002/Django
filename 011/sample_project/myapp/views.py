from django.shortcuts import render

# Create your views here.

def myapp_index(request):
    return render(request,'index.html')

def myapp_about(request):
    return render(request,'about.html')

def myapp_contact(request):
    return render(request,'contact.html')

def myapp_home(request):
    return render(request,'myapp_home.html')