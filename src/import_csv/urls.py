from django.urls import path
from.views import import_file_view, assign_movies
app_name = 'import_csv'

urlpatterns = [
    path('', import_file_view, name='upload-view'),
    path('assign-movies', assign_movies, name='movies')
]
