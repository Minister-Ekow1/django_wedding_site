from django.contrib import admin
from .models import About, Venue, LoveStoryEvent, AboutImage

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ('about', 'image')
    search_fields = ('about__title',)

admin.site.register(Venue)

@admin.register(LoveStoryEvent)
class LoveStoryEventAdmin(admin.ModelAdmin):
    list_display = ("order", "title")
    ordering = ("order",)