from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Note

# Create your views here.
def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': allnotes})   

def note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'notes/note.html', {'note':note}) 
