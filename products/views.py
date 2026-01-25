from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import Product, Category

def product_list(request, slug=None):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)

    selected_category = None
    if slug:
        selected_category = Category.objects.get(slug=slug)
        products = products.filter(category=selected_category)

    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": selected_category
    })

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "products/product_list.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "products/product_detail.html", {"product": product})