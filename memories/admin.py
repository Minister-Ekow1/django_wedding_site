from django.contrib import admin
from .models import Memory

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    actions = ['approve_memories']

    def approve_memories(self, request, queryset):
        queryset.update(is_approved=True)