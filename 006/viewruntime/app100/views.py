from django.shortcuts import render,HttpResponse

# Create your views here.
def sample_runtime(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    age = request.GET.get("age")
    college =request.GET.get("college")
    return HttpResponse(f"ID: {id},  My Name is : {name} and My age is {age} and I Studied in {college}")
