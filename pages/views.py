from django.shortcuts import render
from datetime import datetime

WEDDING_DATE = datetime(2026, 4, 25)

def home(request):
    return render(request, 'pages/home.html', {
        'wedding_date': WEDDING_DATE
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    venue = {
        "name": "Wedding Venue",
        "embed_url": "https://www.google.com/maps/embed?pb=!1m18..."
    }
    return render(request, 'pages/contact.html', {'venue': venue})

def venue(request):
    return render(request, "pages/venue.html")