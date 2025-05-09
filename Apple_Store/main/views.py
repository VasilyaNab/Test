from django.shortcuts import render, get_object_or_404
from .models import *

def StorePage(request):
    products = Product.objects.filter(store__quantity__gt=0).select_related('category', 'store')
    return render(request, 'Warehouse.html', {'products': products})

def ProductDetail(request, pk):
    product = get_object_or_404(Product.objects.filter(store__quantity__gt=0), pk=pk)
    quantity = product.store
    
    return render(request, 'Details.html', {
        'product': product,
        'quantity': quantity,
    })