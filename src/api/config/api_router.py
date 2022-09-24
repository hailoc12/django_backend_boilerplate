from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter, re_path
from django.urls import path, include 
from veminhhoa.users.api.views import UserViewSet
from veminhhoa.render_image.api.views import (
    render_image_from_prompt, RenderTemplateViewset, estimate_render_price,
    RenderTransactionViewset
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("render_template", RenderTemplateViewset)
router.register("render_transaction", RenderTransactionViewset)
urlpatterns = router.urls

urlpatterns += [
    path("render_image/", view=render_image_from_prompt, name="render_image"),
    path("estimate_render_price/", view=estimate_render_price, name="estimate_render_price"),
    path('api-auth/', include('rest_framework.urls'))
]
