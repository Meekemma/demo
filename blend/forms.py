from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *

class DemoForm(ModelForm):
    class Meta:
        model=Demo
        fields=['email']


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['email', 'message']


class NewsletterForm(ModelForm):
    class Meta:
        model=Newsletter
        fields=['email']


class EmailForm(forms.Form):
    subject =forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=CKEditorWidget(), label="Email content")