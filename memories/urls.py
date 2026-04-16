from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('submit/', views.submit_memory, name='submit_memory'),
]