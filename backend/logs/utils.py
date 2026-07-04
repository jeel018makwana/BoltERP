from .models import ActivityLog


def log_activity(
    user,
    action,
    module,
    description,
):

    ActivityLog.objects.create(
        user=user,
        action=action,
        module=module,
        description=description,
    )