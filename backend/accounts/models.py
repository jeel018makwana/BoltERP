from django.db import models
from common.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser

class Role(TimeStampedModel):
    """
    Stores user roles like Admin, Manager, Sales Executive etc.
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class User(AbstractUser, TimeStampedModel):
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username