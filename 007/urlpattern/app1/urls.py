from django.urls import path
from . import views

urlpatterns =[
    path('sample_name/<str:name>/',views.sample_name),
]