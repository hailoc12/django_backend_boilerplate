from django.urls import path
from veminhhoa.render_image.api.views import (
    render_image_from_prompt

)

urlpatterns = [
    path("render_image/", view=render_image_from_prompt, name="render_image"),
]
