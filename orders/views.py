from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem, Payment
from .utils import log_transaction

@login_required
def checkout(request):
    cart = Cart(request)
    if not cart.cart:
        return redirect("product_list")

    if request.method == "POST":
        city = request.POST.get("city")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            user=request.user,
            city=city,
            address=address,
            phone=phone
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item["product"].name,
                price=item["price"],
                quantity=item["quantity"]
            )

        request.session["cart"] = {}
        return redirect("payment", order_id=order.id)

    return render(request, "orders/checkout.html")
@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == "POST":
        txn_id = request.POST.get("transaction_id")

        Payment.objects.create(
            order=order,
            transaction_id=txn_id
        )

        log_transaction(txn_id)
        order.status = "PAYMENT_SUBMITTED"
        order.save()

        return redirect("order_success")

    return render(request, "orders/payment.html", {"order": order})
@login_required
def order_success(request):
    return render(request, "orders/order_success.html")

from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user  # 🔐 Ownership enforcement
    )
    return render(request, "orders/order_detail.html", {"order": order})