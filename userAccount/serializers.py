from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            "user", "email", "image", "first_name", "last_name", "year", "major", "introduction", "subscriptions",
            "events", "schedule", "tags")

        extra_kwargs = {'password': {'write_only': True}}

    """
    def create(self, validated_data):
        user = models.Profile(email=validated_data['email'], name=validated_data['name'])
        user.save()
    """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User

        fields = (
            "id", "username"
        )
