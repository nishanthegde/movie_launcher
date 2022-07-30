from django.shortcuts import render
from .models import Product


# Create your views here.
def chart_select_view(request):
    return render(request, 'products/main.html', {})
