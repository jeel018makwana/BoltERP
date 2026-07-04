from django.db import models
from django.conf import settings
from common.models import TimeStampedModel


class ActivityLog(TimeStampedModel):

    ACTIONS = (
        ("CREATE", "Create"),
        ("UPDATE", "Update"),
        ("DELETE", "Delete"),
        ("LOGIN", "Login"),
        ("LOGOUT", "Logout"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    action = models.CharField(
        max_length=20,
        choices=ACTIONS,
    )

    module = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.action}"