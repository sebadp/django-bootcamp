"""ECommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from accounts.views import login_view, logout_view, register_view
from django.contrib import admin
from django.urls import include, path
from orders.views import order_checkout_view
from products.views import (
    home_view,
    product_create_view,
    product_detail_view,
    product_list_view,
    search_view,
)

urlpatterns = [
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
    path("admin/", admin.site.urls),
    path("home/", home_view, name="home"),
    path("search/", search_view, name="search"),
    path("products/<int:id>", product_detail_view),
    path("products", product_list_view),
    path("products/create", product_create_view),
    path("checkout/", order_checkout_view, name="checkout"),
]
