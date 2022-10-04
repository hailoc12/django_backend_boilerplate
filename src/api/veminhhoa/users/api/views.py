from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .serializers import UserSerializer, PocketSerializer, BillSerializer, NotificationSerializer
from veminhhoa.users.models import Pocket, Bill, Notification
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
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
    def get_queryset(self):
        user = self.request.user
        return Pocket.objects.filter(user=user).all()

    serializer_class = PocketSerializer

class BillViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Bill.objects.filter(pocket=user.pocket).all()
    serializer_class = BillSerializer

    def get_permissions(self):
        if self.request.method == "GET": 
            return [IsAuthenticated()]
        elif self.request.method == "POST":
            return [IsAdminUser()]


class NotificationViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user).all().order_by('-pk')

    serializer_class = NotificationSerializer


