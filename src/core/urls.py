from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls), path("", include("Weather.urls"))]

handler404 = "Weather.views.handler404"
handler500 = "Weather.views.handler500"
