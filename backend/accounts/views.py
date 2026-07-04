from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from common.responses import success_response
from .serializers import (UserSerializer, LoginSerializer, EmployeeSerializer,)
from rest_framework.generics import ListCreateAPIView
from .permissions import IsAdminUserRole
from .models import User
from drf_spectacular.utils import extend_schema
from logs.utils import log_activity

@extend_schema(
    responses={200: UserSerializer},
    tags=["Authentication"],
)
class ProfileAPIView(APIView):
    """
    Returns the currently logged-in user's profile.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return success_response(
            data=serializer.data,
            message="Profile fetched successfully."
        )

@extend_schema(
    request = LoginSerializer,
    responses={200: UserSerializer},
    tags=["Authentication"],
)  
class LoginAPIView(APIView):
    """
    Custom Login API
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        log_activity(
            user=user,
            action="LOGIN",
            module="Authentication",
            description=f"{user.username} logged in.",
        )

        user_data = UserSerializer(user).data

        return success_response(
            message="Login successful.",
            data={
                "user": user_data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            status_code=status.HTTP_200_OK,
        )


@extend_schema(
    request=EmployeeSerializer,
    responses={200: EmployeeSerializer},
    tags=["Employees"],
)
class EmployeeListCreateAPIView(ListCreateAPIView):
    """
    Admin can view all employees and create new employees.
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUserRole]