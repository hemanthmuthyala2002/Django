from django.urls import path
from . import views
urlpatterns =[
    path('staticimage/',views.staicimage, name='staticimage'),
]