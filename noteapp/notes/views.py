from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {
        'notes': notes,
    })

def note_details(request, note_id):
    return HttpResponse(f'<p>note_details view with id {note_id}</p>')
