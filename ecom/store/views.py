
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Cateogary, Product


def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request,'search.html', {
        'query':query,
        'products':products,
    })

def category_detail(request, slug):
    category = get_object_or_404(Cateogary, slug=slug)
    products = category.products.all()
    return render(request, 'category_detail.html' ,{
        'category':category,
        'products':products
    })


def product_detail(request, category_slug,  slug):
    product = get_object_or_404(Product, slug = slug)

    return render(request,'product_detail.html',{
        'product':product
    })