from django.contrib.auth.models import User
from django.db import models


class Csv(models.Model):
    file_name = models.FileField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"File: {self.file_name}"


class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    movie_name = models.TextField()
    movie_user = models.ForeignKey(
        User, null=True, blank=True, default=None, on_delete=models.SET_NULL
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movie name: {self.movie_name}"
