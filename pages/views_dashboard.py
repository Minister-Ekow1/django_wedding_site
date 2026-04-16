from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from memories.models import Memory
from rsvp.models import RSVP
from guestbook.models import GuestMessage

def is_couple(user):
    return user.is_staff

@login_required
@user_passes_test(is_couple)
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {
        'memories': Memory.objects.count(),
        'pending': Memory.objects.filter(is_approved=False).count(),
        'rsvps': RSVP.objects.order_by('-created_at')[:10],
        'messages': GuestMessage.objects.order_by('-created_at')[:10],
    })