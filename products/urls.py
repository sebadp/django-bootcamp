from django.urls import path, include

from products import views


urlpatterns = [
    path('', views.home_view, name="home"),

]
