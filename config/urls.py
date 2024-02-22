
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appinmobiliaria.urls")),
    path("users/", include("users.urls",namespace="users")),
]
