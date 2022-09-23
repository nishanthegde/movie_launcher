from django.contrib import admin
from .models import Csv, Movie, Profile

# Register your models here.

admin.site.register(Csv)
admin.site.register(Movie)
admin.site.register(Profile)
