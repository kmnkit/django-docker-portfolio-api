from rest_framework import serializers as sz
from .models import Achievement
from users.serializers import UserSerializer


class AchievementSerializer(sz.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Achievement
        exclude = ("created_at", "updated_at")
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        achievement = Achievement.objects.create(user=user, **validated_data)
        return achievement
