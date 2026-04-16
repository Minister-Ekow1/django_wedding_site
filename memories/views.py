from django.shortcuts import render, redirect
from .models import Memory
from .forms import MemoryForm
from django.contrib import messages

def gallery(request):
    memories = Memory.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'memories/gallery.html', {'memories': memories})

def submit_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.is_approved = False
            memory.save()

            messages.success(request, "Your memory has been submitted 💕")
            return redirect('gallery')
    else:
        form = MemoryForm()

    return render(request, 'memories/submit.html', {'form': form})