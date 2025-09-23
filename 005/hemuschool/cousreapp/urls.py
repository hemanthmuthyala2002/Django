from django.urls import path
from .import views

urlpatterns= [
    path('view1/', views.sample_view1),
]