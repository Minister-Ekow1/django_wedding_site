from django.shortcuts import render
from .models import Event, ProgramSettings

def program(request):
    events = Event.objects.all()
    settings = ProgramSettings.objects.first()

    return render(request, 'program/program.html', {
        'events': events,
        'settings': settings
    })