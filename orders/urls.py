from django.urls import path
from .views import (
    checkout, payment, order_success,
    order_list, order_detail
)

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("payment/<int:order_id>/", payment, name="payment"),
    path("success/", order_success, name="order_success"),

    path("my/", order_list, name="order_list"),
    path("my/<int:order_id>/", order_detail, name="order_detail"),
]