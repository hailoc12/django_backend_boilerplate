from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter, re_path
from django.urls import path, include 
from veminhhoa.users.api.views import UserViewSet
from veminhhoa.render_image.api.views import render_image_from_prompt, RenderTemplateViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("render_template", RenderTemplateViewset)
urlpatterns = router.urls

urlpatterns += [
    path("render_image/", view=render_image_from_prompt, name="render_image"),
    path('api-auth/', include('rest_framework.urls'))
]
