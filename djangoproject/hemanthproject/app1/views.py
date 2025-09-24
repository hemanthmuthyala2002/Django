from django.shortcuts import render

def home_view(request):
    return render(request, 'app1/home.html')

def login_view(request):
    return render(request, 'app1/login.html')

def register_view(request):
    return render(request, 'app1/register.html')

