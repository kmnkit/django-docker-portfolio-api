from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView

app_name = "users"

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [path("login/", LoginView.as_view())]

urlpatterns += router.urls
