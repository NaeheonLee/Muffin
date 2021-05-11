from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generic', views.generic, name='generic'),
    path('elements', views.elements, name='elements'),
]