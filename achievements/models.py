from django.db import models
from core.models import TimeStampedModel


class Achievement(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="achievements", on_delete=models.CASCADE
    )
    url = models.URLField(max_length=150, blank=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.title} : {self.url}"
