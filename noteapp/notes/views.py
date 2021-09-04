from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Note
from .forms import AddNoteForm, ShareNoteForm

def home(request):
    notes = Note.objects.all()
    viewed_notes = []
    for note in notes:
        if note.check_permission(request.user):
            viewed_notes.append(note)

    return render(request, 'home.html', {
        'notes': viewed_notes,
    })

@login_required
def note_details(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    return render(request, 'note_details.html', {
        'note': note,
    })

@login_required
def add_note(request):
    if request.method == "POST":
        filled_form = AddNoteForm(request.POST)
        if filled_form.is_valid():
            title = filled_form.cleaned_data['title']
            content = filled_form.cleaned_data['content']
            expiration = filled_form.cleaned_data['expiration']
            note = Note()
            note.title = title
            note.content = content
            note.owner = request.user
            note.expiration_date = expiration
            note.save()
            return redirect(f'/note/{note.id}/')

    form = AddNoteForm()
    return render(request, 'add_note.html', {
        'form': form,
    })

def remove_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        if request.method == "POST":
            note.delete()
            return redirect('/')

    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    return render(request, 'note_details.html', {
        'note': note,
    })

def edit_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        if request.method == "POST":
            filled_form = AddNoteForm(request.POST)
            if filled_form.is_valid():
                title = filled_form.cleaned_data['title']
                content = filled_form.cleaned_data['content']
                expiration = filled_form.cleaned_data['expiration']
                note.title = title
                note.content = content
                note.expiration_date = expiration
                note.save()
                return redirect(f'/note/{note.id}/')
        current_note = {
            'title': note.title,
            'content': note.content,
        }
        form = AddNoteForm(initial=current_note)
    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    return render(request, 'edit_note.html', {
        'form': form,
        'note': note,
    })

def share_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
        if request.method == "POST":
            filled_form = ShareNoteForm(request.POST)
            if filled_form.is_valid():
                username = filled_form.cleaned_data['username']
                user = User.objects.get(username=username)
                print(user.id)
                note.share_note(user.id)
                note.save()
                return redirect(f'/note/{note.id}/')
        form = ShareNoteForm()

    except Note.DoesNotExist:
        raise Http404('Note does not exist')

    return render(request, 'share_note.html', {
        'form': form,
        'note': note,
    })

