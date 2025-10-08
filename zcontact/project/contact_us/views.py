from django.shortcuts import render, redirect
from.models import Contact



def contactus(request):
    if request.method == 'POST':
        # Get form data safely
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        place = request.POST.get('place', '').strip()
        user_subject = request.POST.get('user_subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Save to database
        contact = Contact(
            name=name,
            email=email,
            message=message,
            # You can add more fields if you extend your model
            # e.g., phone=phone, place=place, subject=user_subject
        )
        contact.save()

        # Redirect to success page
        return redirect('success')

    # GET request, just show the form
    return render(request, 'contact_us.html')
def success(request):
    return render(request, 'success.html')

