from django.urls import path
from .views import myapp_index, myapp_about, myapp_contact, myapp_home

urlpatterns = [
    path('', myapp_index, name='myapp_index'),
    path('about/', myapp_about, name='myapp_about'),
    path('contact/', myapp_contact, name='myapp_contact'),
    path('home/', myapp_home, name='myapp_home'),
]