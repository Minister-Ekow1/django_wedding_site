from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from pages.models import (
    About,
    AboutImage,
    Venue,
    LoveStoryEvent,
    SiteSettings
)

from program.models import (
    ProgramOutline,
    Event
)

from rsvp.models import RSVP
from guestbook.models import GuestMessage
from memories.models import Memory

from .forms import (
    AboutForm,
    AboutImageForm,
    VenueForm,
    ProgramOutlineForm,
    LoveStoryEventForm,
    EventForm,
    SiteSettingsForm
)


# ======================================================
# DASHBOARD
# ======================================================

@login_required
@staff_member_required
def dashboard(request):

    context = {

        "rsvp_count": RSVP.objects.count(),

        "attending_count": RSVP.objects.filter(
            attending=True
        ).count(),

        "guestbook_count": GuestMessage.objects.count(),

        "memory_count": Memory.objects.count(),

        "approved_memories": Memory.objects.filter(
            is_approved=True
        ).count(),

        "approved_messages": GuestMessage.objects.filter(
            approved=True
        ).count(),

        "pending_guestbook": GuestMessage.objects.filter(
            approved=False
        ).count(),

        "pending_memories": Memory.objects.filter(
            is_approved=False
        ).count(),

        "recent_rsvps": RSVP.objects.order_by(
            "-created_at"
        )[:5],

        "recent_guestbook": GuestMessage.objects.order_by(
            "-created_at"
        )[:5],

        "recent_memories": Memory.objects.order_by(
            "-created_at"
        )[:5],
    }

    return render(
        request,
        "custom_admin/dashboard.html",
        context
    )


# ======================================================
# ABOUT
# ======================================================

@login_required
@staff_member_required
def about_manage(request):

    about = About.objects.first()

    if not about:

        about = About.objects.create(
            title="Our Love Story",
            story=""
        )

    form = AboutForm(
        request.POST or None,
        instance=about
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "About page updated successfully 💖"
        )

        return redirect(
            "custom_admin:about_manage"
        )

    return render(
        request,
        "custom_admin/about.html",
        {
            "form": form
        }
    )


# ======================================================
# ABOUT IMAGES
# ======================================================

@login_required
@staff_member_required
def about_images(request):

    about = About.objects.first()

    images = []

    if about:
        images = about.images.all()

    return render(
        request,
        "custom_admin/about_images.html",
        {
            "images": images
        }
    )


@login_required
@staff_member_required
def about_image_add(request):

    about = About.objects.first()

    if not about:

        about = About.objects.create(
            title="Our Love Story",
            story=""
        )

    form = AboutImageForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        image = form.save(commit=False)

        image.about = about

        image.save()

        messages.success(
            request,
            "About image added successfully 📸"
        )

        return redirect(
            "custom_admin:about_images"
        )

    return render(
        request,
        "custom_admin/about_image_form.html",
        {
            "form": form,
            "title": "Add About Image"
        }
    )


@login_required
@staff_member_required
def about_image_edit(request, id):

    image = get_object_or_404(
        AboutImage,
        id=id
    )

    form = AboutImageForm(
        request.POST or None,
        request.FILES or None,
        instance=image
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "About image updated 📸"
        )

        return redirect(
            "custom_admin:about_images"
        )

    return render(
        request,
        "custom_admin/about_image_form.html",
        {
            "form": form,
            "title": "Edit About Image"
        }
    )


@login_required
@staff_member_required
def about_image_delete(request, id):

    image = get_object_or_404(
        AboutImage,
        id=id
    )

    if request.method == "POST":

        image.delete()

        messages.success(
            request,
            "About image deleted"
        )

        return redirect(
            "custom_admin:about_images"
        )

    return render(
        request,
        "custom_admin/about_image_delete.html",
        {
            "image": image
        }
    )


# ======================================================
# VENUE
# ======================================================

@login_required
@staff_member_required
def venue_manage(request):

    venue = Venue.objects.first()

    if not venue:

        venue = Venue.objects.create(
            name="Wedding Venue",
            address="",
            embed_url=""
        )

    form = VenueForm(
        request.POST or None,
        instance=venue
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Venue updated successfully 📍"
        )

        return redirect(
            "custom_admin:venue_manage"
        )

    return render(
        request,
        "custom_admin/venue.html",
        {
            "form": form
        }
    )


# ======================================================
# LOVE STORY
# ======================================================

@login_required
@staff_member_required
def love_story_manage(request):

    events = LoveStoryEvent.objects.all()

    return render(
        request,
        "custom_admin/love_story.html",
        {
            "events": events
        }
    )


@login_required
@staff_member_required
def love_story_add(request):

    form = LoveStoryEventForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Love story event added 💖"
        )

        return redirect(
            "custom_admin:love_story_manage"
        )

    return render(
        request,
        "custom_admin/love_story_form.html",
        {
            "form": form
        }
    )


@login_required
@staff_member_required
def love_story_edit(request, id):

    event = get_object_or_404(
        LoveStoryEvent,
        id=id
    )

    form = LoveStoryEventForm(
        request.POST or None,
        instance=event
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Love story event updated 💖"
        )

        return redirect(
            "custom_admin:love_story_manage"
        )

    return render(
        request,
        "custom_admin/love_story_form.html",
        {
            "form": form
        }
    )


@login_required
@staff_member_required
def love_story_delete(request, id):

    event = get_object_or_404(
        LoveStoryEvent,
        id=id
    )

    if request.method == "POST":

        event.delete()

        messages.success(
            request,
            "Love story event deleted"
        )

        return redirect(
            "custom_admin:love_story_manage"
        )

    return render(
        request,
        "custom_admin/love_story_delete.html",
        {
            "event": event
        }
    )


# ======================================================
# PROGRAM
# ======================================================

@login_required
@staff_member_required
def program_manage(request):

    outline = ProgramOutline.objects.first()

    if not outline:
        outline = ProgramOutline.objects.create()

    form = ProgramOutlineForm(
        request.POST or None,
        request.FILES or None,
        instance=outline
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Program updated successfully 📅"
        )

        return redirect(
            "custom_admin:program_manage"
        )

    events = Event.objects.all()

    return render(
        request,
        "custom_admin/program.html",
        {
            "form": form,
            "events": events
        }
    )


@login_required
@staff_member_required
def program_add(request):

    form = EventForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Program event added 📅"
        )

        return redirect(
            "custom_admin:program_manage"
        )

    return render(
        request,
        "custom_admin/program_form.html",
        {
            "form": form
        }
    )


@login_required
@staff_member_required
def program_edit(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    form = EventForm(
        request.POST or None,
        instance=event
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Program event updated 📅"
        )

        return redirect(
            "custom_admin:program_manage"
        )

    return render(
        request,
        "custom_admin/program_form.html",
        {
            "form": form
        }
    )


@login_required
@staff_member_required
def program_delete(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    if request.method == "POST":

        event.delete()

        messages.success(
            request,
            "Program event deleted"
        )

        return redirect(
            "custom_admin:program_manage"
        )

    return render(
        request,
        "custom_admin/program_delete.html",
        {
            "event": event
        }
    )


# ======================================================
# RSVP
# ======================================================

@login_required
@staff_member_required
def rsvp_manage(request):

    rsvps = RSVP.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "custom_admin/rsvp.html",
        {
            "rsvps": rsvps
        }
    )


@login_required
@staff_member_required
def rsvp_detail(request, id):

    rsvp = get_object_or_404(
        RSVP,
        id=id
    )

    return render(
        request,
        "custom_admin/rsvp_detail.html",
        {
            "rsvp": rsvp
        }
    )


# ======================================================
# GUESTBOOK
# ======================================================

@login_required
@staff_member_required
def guestbook_manage(request):

    messages_list = GuestMessage.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "custom_admin/guestbook.html",
        {
            "messages": messages_list
        }
    )


@login_required
@staff_member_required
def guestbook_approve(request, id):

    message = get_object_or_404(
        GuestMessage,
        id=id
    )

    message.approved = not message.approved
    message.save()

    messages.success(
        request,
        "Guestbook approval updated"
    )

    return redirect(
        "custom_admin:guestbook_manage"
    )


@login_required
@staff_member_required
def guestbook_delete(request, id):

    message = get_object_or_404(
        GuestMessage,
        id=id
    )

    if request.method == "POST":

        message.delete()

        messages.success(
            request,
            "Guestbook message deleted"
        )

        return redirect(
            "custom_admin:guestbook_manage"
        )

    return render(
        request,
        "custom_admin/guestbook_delete.html",
        {
            "message": message
        }
    )


# ======================================================
# MEMORIES
# ======================================================

@login_required
@staff_member_required
def memories_manage(request):

    memories = Memory.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "custom_admin/memories.html",
        {
            "memories": memories
        }
    )


@login_required
@staff_member_required
def memory_detail(request, id):

    memory = get_object_or_404(
        Memory,
        id=id
    )

    return render(
        request,
        "custom_admin/memory_detail.html",
        {
            "memory": memory
        }
    )


@login_required
@staff_member_required
def memory_approve(request, id):

    memory = get_object_or_404(
        Memory,
        id=id
    )

    memory.is_approved = not memory.is_approved
    memory.save()

    messages.success(
        request,
        "Memory approval updated"
    )

    return redirect(
        "custom_admin:memories_manage"
    )


@login_required
@staff_member_required
def memory_delete(request, id):

    memory = get_object_or_404(
        Memory,
        id=id
    )

    if request.method == "POST":

        memory.delete()

        messages.success(
            request,
            "Memory deleted"
        )

        return redirect(
            "custom_admin:memories_manage"
        )

    return render(
        request,
        "custom_admin/memory_delete.html",
        {
            "memory": memory
        }
    )


# ======================================================
# SITE SETTINGS
# ======================================================

@login_required
@staff_member_required
def site_settings_manage(request):

    settings = SiteSettings.objects.first()

    if not settings:

        settings = SiteSettings.objects.create(
            site_name="Wedding Site",
            bride_name="Bride",
            groom_name="Groom"
        )

    form = SiteSettingsForm(
        request.POST or None,
        request.FILES or None,
        instance=settings
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Site settings updated ⚙️"
        )

        return redirect(
            "custom_admin:site_settings_manage"
        )

    return render(
        request,
        "custom_admin/site_settings.html",
        {
            "form": form
        }
    )