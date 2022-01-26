from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    fields = ("title", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "text")
