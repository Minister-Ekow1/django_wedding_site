from django.urls import path
from .views import guestbook

urlpatterns = [
    path('', guestbook, name='guestbook'),
]