from django.shortcuts import render
from .forms import CsvForm
from .models import Csv, Movie
import csv
from django.contrib.auth.models import User


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
                    for row in reader:
                        movie, _ = Movie.objects.get_or_create(movie_id=row[0], movie_name=row[1])

                obj.success = True
                obj.save()

                success_message = "File uploaded successfully"

            except Exception as exc:
                error_message = "Oops.. something went wrong: " + str(exc)

    else:
        form = CsvForm()

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    }
    return render(request, 'import/upload.html', context)
