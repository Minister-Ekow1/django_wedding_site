from django.shortcuts import render
from .models import ProgramEvent

def program_view(request):
    events = ProgramEvent.objects.all().order_by('time')
    return render(request, 'program/program.html', {'events': events})