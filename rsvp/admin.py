from django.contrib import admin
from .models import RSVP, RSVPContact  # Import RSVPContact

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'attending', 'guests')
    search_fields = ("name", "email")
    ordering = ("-id",)

@admin.register(RSVPContact)
class RSVPContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ("name", "email", "phone")
    ordering = ("name",)