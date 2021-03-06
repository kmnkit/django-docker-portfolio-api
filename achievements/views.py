from rest_framework.viewsets import ModelViewSet
from .serializers import AchievementSerializer
from .models import Achievement


class AchievementViewSet(ModelViewSet):
    queryset = Achievement.objects.select_related("user").all()
    serializer_class = AchievementSerializer
