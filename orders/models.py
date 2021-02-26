from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, pre_save
from products.models import Product

# Create your models here.

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ("created", "Created"),
    ("stale", "Stale"),
    ("paid", "Paid"),
    ("shipped", "Shipped"),
    ("refunded", "Refunded"),
)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="created")
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    inventory_updated = models.BooleanField(default=False)

    def mark_paid(self, custom_amount=None, save=False):
        paid_amount = self.total
        if custom_amount != None:
            paid_amount = custom_amount
        self.paid = paid_amount
        self.status = 'paid'
        if not self.inventory_updated and instance.product:
            instance.product.remove_item_from_inventory(save=True)

            self.inventory_updated = True
        if save == True:
            self.save()
        retunr self.paid

    def calculate(self):
        if not self.product:
            return {}
        subtotal = self.product.price
        tax_rate = Decimal(0.12)
        tax_total = tax_rate * subtotal
        tax_total = Decimal("%.2f" % (tax_total))
        total = subtotal + tax_total
        total = Decimal("%2f" % (total))
        totals = {"subtotal": subtotal, "tax": tax_total, "total": total}

        for k, v in totals.items():
            setattr(self, k, v)
            if save == True:
                self.save()
        return totals


def order_pre_save(sender, instance, *args, **kwargs):
    instance.calculate(save=False)


pre_save.conect(order_pre_save, sender=Order)
