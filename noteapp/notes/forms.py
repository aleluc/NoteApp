from django import forms
from django.forms.widgets import Widget

class AddNoteForm(forms.Form):
    title = forms.CharField(label='Enter title:', widget=forms.TextInput)
    content = forms.CharField(label='Enter content:', widget=forms.Textarea)

class ShareNoteForm(forms.Form):
    username = forms.CharField(label='Share with:', widget=forms.TextInput)
