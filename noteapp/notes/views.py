from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<p>home view</p>')

def note_details(request, note_id):
    return HttpResponse(f'<p>note_details view with id {note_id}</p>')
