from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("users.urls", namespace="users")),
    path(
        "api/v1/achievements/", include("achievements.urls", namespace="achievements")
    ),
]
