from django.urls import path
from .views import rsvp_view

urlpatterns = [
    path('', rsvp_view, name='rsvp'),
]