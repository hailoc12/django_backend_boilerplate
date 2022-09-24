from rest_framework import serializers
from veminhhoa.render_image.models import RenderTemplate

class RenderTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderTemplate
        fields = ['id', 'name', 'description']