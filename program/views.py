from django.shortcuts import render
from .models import Event, ProgramOutline

def program(request):
    events = Event.objects.all()
    outline = ProgramOutline.objects.first()

    return render(request, 'program/program.html', {
        'events': events,
        'outline': outline,
    })