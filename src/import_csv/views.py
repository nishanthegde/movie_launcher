from django.shortcuts import render
from .forms import CsvForm, AssignMovieForm
from .models import Movie
import csv
from django.contrib.auth.models import User
from django.forms import modelformset_factory


# Create your views here.
def import_file_view(request):
    error_message = None
    success_message = None

    if request.method == "POST":
        form = CsvForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            try:
                with open(obj.file_name.path, 'r') as f:
                    reader = csv.reader(f)
                    row_cnt = 0
                    for row in reader:
                        movie, _ = Movie.objects.get_or_create(movie_id=row[0], movie_name=row[1])
                        row_cnt += 1

                obj.success = True
                obj.save()

                if row_cnt > 1:
                    tag = "rows"
                else:
                    tag = "row"

                success_message = f"File uploaded successfully: {row_cnt} {tag} imported"

            except Exception as exc:
                error_message = f"File import error: {str(exc)}"

    else:
        form = CsvForm()

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    }
    return render(request, 'import/upload.html', context)


def reset_movies():
    movies = Movie.objects.all()

    for movie in movies:
        movie.movie_user = None
        movie.save()


def assign_movies_view(request):
    error_message = None
    AssignMovieFormSet = modelformset_factory(Movie, form=AssignMovieForm)
    formset = None

    if request.method == 'POST':

        if Movie.objects.count() == 0:
            error_message = f"Import movies first!"
        else:
            if "assign" in request.POST:
                formset = AssignMovieFormSet(request.POST)
                formset.clean()
                for form in formset:
                    movie_id = form.cleaned_data.get("movie_id", None)
                    movie_user = form.cleaned_data.get("movie_user", None)

                    if form.has_changed():
                        movie = Movie.objects.get(movie_id=movie_id)
                        movie.movie_user = movie_user
                        movie.save()
            else:
                reset_movies()
                formset = AssignMovieFormSet()
    else:
        formset = AssignMovieFormSet()

    context = {
        'formset': formset,
        'error_message': error_message
    }
    return render(request, 'import/assign_movies.html', context)
