from django.contrib.auth import get_user_model
from rest_framework import serializers
from veminhhoa.users.models import Pocket, Bill, Notification

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class PocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocket
        fields = ['user', 'balance']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['amount', 'name', 'description', 'has_processed']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['name', 'detail', 'has_sent', 'has_read', 'created']