from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter, re_path
from django.urls import path 

from bot_xsmb.users.api.views import UserViewSet
from bot_xsmb.bots.api.views import FreeViberBotCallbackView, PremiumViberBotCallbackView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path('free_viber_callback/', FreeViberBotCallbackView.as_view()),
    path('free_test_viber_callback/', FreeViberBotCallbackView.as_view()),
    path('premium_viber_callback/', PremiumViberBotCallbackView.as_view()),
    path('premium_test_viber_callback/', PremiumViberBotCallbackView.as_view()),
]
