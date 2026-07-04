from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = (
        "created_at",
        "user",
        "action",
        "module",
    )

    search_fields = (
        "module",
        "description",
    )

    list_filter = (
        "action",
        "module",
    )

    ordering = (
        "-created_at",
    )