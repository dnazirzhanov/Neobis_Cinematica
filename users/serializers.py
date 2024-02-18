from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Feedback, BonusCard


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User(username=validated_data["username"])
            user.set_password(validated_data["password"])
            user.save()
            return user


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class BonusCardSerializer(ModelSerializer):
    class Meta:
        model = BonusCard
        fields = "__all__"


