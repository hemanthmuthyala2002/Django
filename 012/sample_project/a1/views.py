from django.shortcuts import render

# Create your views here.
def a1_index(request):
    return render(request,'index.html')
def a1_about(request):
    return render(request,'about.html')
def a1_contact(request):
    return render(request,'contact.html')
def a1_home(request):
    return render(request,'a1_home.html')
