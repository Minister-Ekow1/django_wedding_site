from django.contrib import admin
from .models import ProgramEvent

@admin.register(ProgramEvent)
class ProgramEventAdmin(admin.ModelAdmin):
    list_display = ('time', 'title')