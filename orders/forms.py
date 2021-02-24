from django import forms

from .models import Order


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = [
            "shipping_address",
            "billing_address",
        ]
