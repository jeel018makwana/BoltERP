from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user information.
    """

    role = serializers.CharField(source= "role.name", read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "employee_id",
            "role",
        ]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            username = username,
            password = password,
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password."
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                "User Account is inactive"
            )
        
        attrs["user"] = user
        return attrs


class EmployeeSerializer(serializers.ModelSerializer):

    role_name = serializers.CharField(
        source="role.name",
        read_only=True
    )

    password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "employee_id",
            "phone",
            "role",
            "role_name",
            "is_active",
        ]

    def create(self, validated_data):

        password = validated_data.pop("password", "password123")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user