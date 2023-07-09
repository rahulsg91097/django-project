from django.forms import ModelForm
from django import forms
from .models import Movie

class UploadForm(ModelForm):
    title = forms.TextInput()
    year = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = Movie
        fields = ['title', 'year', 'image']