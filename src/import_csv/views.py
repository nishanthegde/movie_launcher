from django.shortcuts import render
from .forms import CsvForm
from .models import Csv, Movie
import csv
from django.contrib.auth.models import User


# Create your views here.
def import_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvForm()

        try:
            obj = Csv.objects.get(activated=False)

            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    user = User.objects.get(id=row[2])
                    movie, _ = Movie.objects.get_or_create(movie_id=row[0], movie_name=row[1])

            obj.activated = True
            obj.save()
            success_message = "File uploaded successfully"
        except:
            error_message = "Oops.. something went wrong!"

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    }
    return render(request, 'import/upload.html', context)
