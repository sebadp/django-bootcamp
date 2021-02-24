from django.contrib import admin
from products.models import Product
from profiles.models import Profile 
# Register your models here.

admin.site.register(Product)
admin.site.register(Profile)