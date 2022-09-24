from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from veminhhoa.render_image.business import RenderManager
from veminhhoa.render_image.models import RenderTemplate
from veminhhoa.render_image.serializers import RenderTemplateSerializer
import json

class RenderImageFromPromptView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        """Create new render transaction"""
        """
            @Args:
                - raw_prompt
                - render_template_id
                - see other args in veminhhoa.render_image.lib.stable_diffusion.render_image()
        """
        data = request.data
        raw_prompt = data['raw_prompt'] if 'raw_prompt' in data else None
        render_template_id = data['render_template_id'] if 'render_template_id' in data else None 

        if (not raw_prompt) or (not render_template_id):
            return Response("Missing raw_prompt or render_template_id", 400)
        
        image_urls, status_code = RenderManager.render_images_from_user_prompt(raw_prompt, render_template_id, data)
        if image_urls: 
            return Response(
                {"status": status_code, 
                "images": image_urls}, 200)
        else:
            return Response(
                {
                    "status": status_code
                }, 200)

render_image_from_prompt = RenderImageFromPromptView.as_view()

class RenderTemplateViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RenderTemplateSerializer
    queryset = RenderTemplate.objects.all()


