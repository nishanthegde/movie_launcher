from django import forms
from .models import Csv
from django.contrib.auth.models import User

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
