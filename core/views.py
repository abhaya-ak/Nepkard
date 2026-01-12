from django.shortcuts import render
from products.models import Product

def home(request):
    top_products = Product.objects.filter(
        is_active=True,
        stock__gt=0
    ).order_by("-created_at")[:4]

    return render(request, "core/home.html", {
        "top_products": top_products
    })
