from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "created_at",
    ]

    search_fields = [
        "name",
    ]

    ordering = [
        "name",
    ]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "employee_id",
        "phone",
        "role",
        "is_staff",
        "is_active",
    ]

    list_filter = [
        "role",
        "is_staff",
        "is_active",
    ]

    search_fields = [
        "username",
        "email",
        "employee_id",
        "phone",
    ]

    ordering = [
        "username",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            "ERP Information",
            {
                "fields": (
                    "employee_id",
                    "phone",
                    "profile_picture",
                    "role",
                ),
            },
        ),
    )