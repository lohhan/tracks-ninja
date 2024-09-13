from django.contrib import admin
from django.urls import path, include
import track.urls
from track.api import api


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(track.urls)),
    path("api/", api.urls)
]
