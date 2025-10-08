from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'app1/home.html')

def login_view(request):
    if request.method == 'POST':
        return redirect('home')  # placeholder
    return render(request, 'app1/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        return redirect('login')
    return render(request, 'app1/register.html')

def contact_view(request):
    success = False
    if request.method == 'POST':
        # collect form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        # You can save data here (DB or email)
        success = True
    return render(request, 'app1/contactus.html', {'success': success})

