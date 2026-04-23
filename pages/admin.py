from django.contrib import admin
from .models import About, Venue, LoveStoryEvent

admin.site.register(About)
admin.site.register(Venue)

@admin.register(LoveStoryEvent)
class LoveStoryEventAdmin(admin.ModelAdmin):
    list_display = ("order", "title")
    ordering = ("order",)