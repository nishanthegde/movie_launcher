from django import forms
from .models import Csv, Movie
from django.contrib.auth.models import User

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


class AssignMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("movie_id", "movie_name", "movie_user")
