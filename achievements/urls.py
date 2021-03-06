from .views import AchievementViewSet
from rest_framework.routers import DefaultRouter

app_name = "achievements"

router = DefaultRouter()
router.register("", AchievementViewSet)

urlpatterns = router.urls
