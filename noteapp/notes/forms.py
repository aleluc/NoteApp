from django import forms
from django.forms.widgets import Widget

class AddForm(forms.Form):
    title = forms.CharField(label='Enter title:', widget=forms.Textarea)
    content = forms.CharField(label='Enter content:', widget=forms.Textarea)