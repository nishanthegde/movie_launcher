from django.db import models


# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return "File id: {}".format(self.id)


class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    movie_name = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Move name: {}".format(self.movie_name)
