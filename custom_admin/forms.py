from django import forms
from pages.models import About, AboutImage, Venue, LoveStoryEvent, SiteSettings
from program.models import ProgramOutline, Event
from rsvp.models import RSVP, RSVPContact
from guestbook.models import GuestMessage
from memories.models import Memory


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


class AboutImageForm(forms.ModelForm):

    class Meta:

        model = AboutImage

        fields = ["image"]

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class LoveStoryEventForm(forms.ModelForm):
    class Meta:
        model = LoveStoryEvent
        fields = '__all__'


class ProgramOutlineForm(forms.ModelForm):
    class Meta:
        model = ProgramOutline
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'


class RSVPContactForm(forms.ModelForm):
    class Meta:
        model = RSVPContact
        fields = '__all__'


class GuestMessageForm(forms.ModelForm):
    class Meta:
        model = GuestMessage
        fields = '__all__'


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = '__all__'

class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = "__all__"