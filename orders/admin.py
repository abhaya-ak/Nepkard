from django.contrib import admin
from .models import Order, OrderItem, Payment

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "price", "quantity")
    can_delete = False


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "transaction_id", "submitted_at")
    search_fields = ("transaction_id",)
    readonly_fields = ("order", "transaction_id", "submitted_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("id", "user__email")
    inlines = [OrderItemInline]

    actions = ["mark_verified", "mark_rejected"]

    def mark_verified(self, request, queryset):
        queryset.update(status="VERIFIED")
    mark_verified.short_description = "Mark selected orders as VERIFIED"

    def mark_rejected(self, request, queryset):
        queryset.update(status="REJECTED")
    mark_rejected.short_description = "Mark selected orders as REJECTED"