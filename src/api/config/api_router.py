from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter, re_path
from django.urls import path 
from veminhhoa.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    # path('free_viber_callback/', FreeViberBotCallbackView.as_view()),
]
