from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .serializers import UserSerializer, PocketSerializer, BillSerializer, NotificationSerializer
from veminhhoa.users.models import Pocket, Bill, Notification
from rest_framework.permissions import AllowAny
User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class PocketViewSet(viewsets.ReadOnlyModelViewSet):
    # user = self.request.user
    permission_classes = [AllowAny]
    serializer_class = PocketSerializer
    queryset = Pocket.objects.all()

class BillViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


