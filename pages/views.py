from django.shortcuts import render
from datetime import datetime
from .models import About, Venue, LoveStoryEvent, AboutImage

WEDDING_DATE = datetime(2027, 5, 10)

def home(request):
    return render(request, 'pages/home.html', {
        'wedding_date': WEDDING_DATE
    })

def about(request):
    about = About.objects.first()
    timeline = LoveStoryEvent.objects.all()
    images = AboutImage.objects.exclude(
    image=""
).exclude(
    image=None
)

    return render(request, 'pages/about.html', {
        'about': about,
        'timeline': timeline,
        'images': images,  # Add this to context
    })

def contact(request):
    venue = Venue.objects.first()
    return render(request, 'pages/contact.html', {'venue': venue})

