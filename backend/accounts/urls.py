from django.urls import path
from .views import (
    LoginAPIView,
    ProfileAPIView,
    EmployeeListCreateAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),

    path(
        "employees/",
        EmployeeListCreateAPIView.as_view(),
        name="employees",
    ),
]
