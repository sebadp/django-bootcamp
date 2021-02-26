from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def has_inventory(self):
        return self.inventory > 0  # Esto devuelve True or False

    def remove_item_from_inventory(self, count=1, save=True):
        current_inv = self.inventory
        current_inv = current_inv - 1
        self.inventory = current_inv
        if save == True:
            self.save()
        return self.inventory
