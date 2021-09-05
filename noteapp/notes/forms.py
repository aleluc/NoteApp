from django import forms
from django.forms.widgets import Widget

class AddNoteForm(forms.Form):
    title = forms.CharField(label='Enter title:', widget=forms.TextInput)
    content = forms.CharField(label='Enter content:', widget=forms.Textarea)
    expires = forms.BooleanField(label='Set expiration date?', widget=forms.CheckboxInput, required=False)
    expiration = forms.DateField(label='Enter expiration date', widget=forms.SelectDateWidget)

class ShareNoteForm(forms.Form):
    username = forms.CharField(label='Share with:', widget=forms.TextInput)
