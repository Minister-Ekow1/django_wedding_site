from django.shortcuts import render, redirect
from .forms import RSVPForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from notifications.utils import notify   # realtime helper

from .models import RSVPContact  # Add this import

def rsvp_view(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)

        if form.is_valid():
            rsvp = form.save()

            # 📧 Email notification
            send_mail(
                subject="New RSVP 💍",
                message=f"{rsvp.name} is attending: {rsvp.attending}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            # 🔔 Real-time notification
            notify(f"New RSVP from {rsvp.name}")

            messages.success(request, "Thank you for your RSVP 💕")
            return redirect('rsvp')

    else:
        form = RSVPForm()

    contacts = RSVPContact.objects.all()  # Add this line

    return render(request, 'rsvp/rsvp.html', {'form': form, 'contacts': contacts})  # Add contacts to context