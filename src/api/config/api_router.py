from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter, re_path
from django.urls import path, include 
from veminhhoa.users.api.views import UserViewSet
from veminhhoa.render_image.api.views import (
    BookViewSet, AuthorViewSet, OrderViewSet, GetBestAuthorView
)
from veminhhoa.users.api.views import (
    PocketViewSet, BillViewSet, NotificationViewSet
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("books", BookViewSet, basename="books")
router.register("authors", AuthorViewSet, basename="authors")
router.register("orders", OrderViewSet, basename="orders")
# router.register("render_template", RenderTemplateViewset, basename='render_template')
# router.register("render_transaction", RenderTransactionViewset, basename='render_transaction')
# router.register("pocket", PocketViewSet, basename='pocket')
# router.register("bill", BillViewSet, basename='bill')
# router.register("notification", NotificationViewSet, basename='notification')
urlpatterns = router.urls

urlpatterns += [
    path ("best_authors/", view = GetBestAuthorView.as_view(), name='get_best_author'), 
    # path("render_image/", view=render_image_from_prompt, name="render_image"),
    # path("estimate_render_price/", view=estimate_render_price, name="estimate_render_price"),
    path('api-auth/', include('rest_framework.urls'))
]
