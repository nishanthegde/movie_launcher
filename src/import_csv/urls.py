from django.urls import path
from .views import import_file_view, assign_movies_view
app_name = 'import_csv'

urlpatterns = [
    path('', import_file_view, name='upload-view'),
    path('assign_movies', assign_movies_view, name='assign-movies'),

]
