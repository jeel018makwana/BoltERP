from rest_framework.permissions import BasePermission


class IsAdminUserRole(BasePermission):
    """
    Only ERP Admin users are allowed.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if user.role:
            return user.role.name.lower() == "admin"

        return False