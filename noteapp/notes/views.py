from django.http.response import Http404, HttpResponse
from django.shortcuts import render

from .models import Note
from .forms import AddForm

def home(request):
    form = AddForm()
    notes = Note.objects.all()
    return render(request, 'home.html', {
        'notes': notes,
        'form': form,
    })

def note_details(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404('Note does not exist')
    return render(request, 'note_details.html', {
        'note': note,
    })
