from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Hemanth"
    friends = ["Chandana", "Maha", "lakshmi"]
    return render(request, "index.html", {"name": name, "friends": friends})

def about(request):
    return render(request, "about.html")

