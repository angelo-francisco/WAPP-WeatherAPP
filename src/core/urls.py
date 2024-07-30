from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls), path("", include("weather.urls"))]

handler404 = "weather.views.handler404"
handler500 = "weather.views.handler500"
