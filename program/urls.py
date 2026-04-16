from django.urls import path
from .views import program_view

urlpatterns = [
    path('', program_view, name='program'),
]