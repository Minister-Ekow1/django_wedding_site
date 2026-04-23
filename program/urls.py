from django.urls import path
from .views import program

urlpatterns = [
    path('', program, name='program'),
]