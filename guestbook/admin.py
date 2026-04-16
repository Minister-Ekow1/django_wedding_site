from django.contrib import admin
from .models import GuestMessage

@admin.register(GuestMessage)
class GuestMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved', 'created_at')
    list_filter = ('approved',)
    actions = ['approve_messages']

    def approve_messages(self, request, queryset):
        queryset.update(approved=True)