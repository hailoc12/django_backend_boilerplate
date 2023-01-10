from rest_framework import serializers
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction, Book, Author, Order

class RenderTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderTemplate
        fields = ['pk', 'name', 'description']

class RenderTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenderTransaction
        fields = ['pk', 'raw_prompt', 'translated_prompt', 'render_template', 'processed_prompt', 'image_urls']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'