from django import forms
from django.forms import widgets
from .models import ShortURL

# Allows for customisation if required
class ShortURLForm(forms.ModelForm):
  long_url = forms.URLField(widget=forms.URLInput(
    attrs={"class": "form-control form-control-lg", 
           "placeholder": "Paste long URL here"}))

  class Meta:
    model = ShortURL
    fields = ('long_url',)
  