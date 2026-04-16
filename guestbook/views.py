from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GuestMessage
from .forms import GuestMessageForm

from notifications.utils import notify

def guestbook(request):
    approved_messages = GuestMessage.objects.filter(approved=True).order_by('-created_at')

    if request.method == 'POST':
        form = GuestMessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)
            msg.approved = False
            msg.save()

            # 🔔 Real-time notification
            notify(f"New guest message from {msg.name}")

            messages.success(request, "Your message is awaiting approval 💕")
            return redirect('guestbook')
    else:
        form = GuestMessageForm()

    return render(request, 'guestbook/guestbook.html', {
        'form': form,
        'messages_list': approved_messages
    })