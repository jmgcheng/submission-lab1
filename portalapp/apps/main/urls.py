from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("restaurants", include("apps.restaurant.urls")),

    path("", include("apps.sample.urls"))             # UI Kits Html files
]
