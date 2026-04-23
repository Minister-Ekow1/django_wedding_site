from django.shortcuts import render
from datetime import datetime
from .models import About, Venue, LoveStoryEvent

WEDDING_DATE = datetime(2026, 4, 25)

def home(request):
    return render(request, 'pages/home.html', {
        'wedding_date': WEDDING_DATE
    })

def about(request):
    about = About.objects.first()
    timeline = LoveStoryEvent.objects.all()

    return render(request, 'pages/about.html', {
        'about': about,
        'timeline': timeline
    })

def contact(request):
    venue = Venue.objects.first()
    return render(request, 'pages/contact.html', {'venue': venue})

