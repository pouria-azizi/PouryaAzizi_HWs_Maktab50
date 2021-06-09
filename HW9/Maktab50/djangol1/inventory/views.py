from django.shortcuts import render
from django.views.generic import ListView
from . import models


class ListProductView(ListView):
    """
    shows a list of active products
    """
    queryset = models.Product.objects.filter(is_active=True)
    # paginate_by = 6
