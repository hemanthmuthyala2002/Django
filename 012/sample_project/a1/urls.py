from django.urls import path
from .views import a1_about,a1_contact,a1_home,a1_index
urlpatterns = [
    path('', a1_index, name='a1_index'),
    path('about/', a1_about, name='a1_about'),
    path('contact/', a1_contact, name='a1_contact'),
    path('home/', a1_home, name='a1_home'),
]