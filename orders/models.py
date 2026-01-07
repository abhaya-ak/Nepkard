from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ("CREATED", "Created"),
        ("PAYMENT_SUBMITTED", "Payment Submitted"),
        ("VERIFIED", "Verified"),
        ("REJECTED", "Rejected"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="CREATED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)