from django.urls import path
from . import views
urlpatterns=[
    path('imageproject/',views.imageproject, name='imageproject')
]