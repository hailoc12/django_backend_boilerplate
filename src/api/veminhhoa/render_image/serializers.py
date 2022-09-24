from rest_framework import serializers
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction

class RenderTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderTemplate
        fields = ['pk', 'name', 'description']

class RenderTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderTransaction
        fields = ['pk', 'raw_prompt', 'translated_prompt', 'render_template', 'processed_prompt', 'image_urls']