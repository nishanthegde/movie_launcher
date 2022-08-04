from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd


# Create your views here.
def chart_select_view(request):
    error_message = None
    context = {}
    df = None

    try:
        product_df = pd.DataFrame(Product.objects.all().values())
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id'] = product_df['id']

        if purchase_df.shape[0] > 0:
            df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1) \
                .rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
            context = {
                'df': df.to_html(),
                'error_message': error_message
            }
        else:
            error_message = 'No records in the database'
            context = {
                'df': df,
                'error_message': error_message
            }
    except:
        product_df = None
        purchase_df = None
        error_message = 'No records in the database'

        # context = {
        #     'df': df,
        #     'error_message': error_message
        # }

    return render(request, 'products/main.html', context)
