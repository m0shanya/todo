from django.shortcuts import render

from notes.forms import AddNoteForm
from notes.models import Note


def notes_index(request):
    notes = []
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
    else:
        form = AddNoteForm()
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes, "form": form})
