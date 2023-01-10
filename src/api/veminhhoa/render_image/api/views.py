from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from veminhhoa.render_image.business import RenderManager
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction, Book, Author, Order
from veminhhoa.render_image.serializers import RenderTemplateSerializer, RenderTransactionSerializer, BookSerializer, AuthorSerializer, OrderSerializer
import json
from django.db.models import Sum

class RenderImageFromPromptView(APIView):
    def post(self, request):
        """Create new render transaction"""
        """
            @Args:
                - raw_prompt
                - render_template_id
                - see other args in veminhhoa.render_image.lib.stable_diffusion.render_image()
        """
        data = request.data
        user = request.user 
        raw_prompt = data['raw_prompt'] if 'raw_prompt' in data else None
        render_template_id = data['render_template_id'] if 'render_template_id' in data else None 
        transaction_id = data['transaction_id'] if 'transaction_id' in data else None

        if (not raw_prompt) or (not render_template_id):
            return Response("Missing raw_prompt or render_template_id", 400)
        
        image_urls, status_code, transaction = RenderManager.render_images_from_user_prompt(user, raw_prompt, render_template_id, transaction_id, data)
        if image_urls and status_code == 0:  # ok 
            RenderManager.process_fee(user, transaction) # create bill & subtract fee & notify

            return Response(
                {"status": status_code, 
                "images": image_urls, 
                "retry_count": transaction.retry_count, 
                "transaction_id": transaction.pk}, 200)
        else:
            if transaction:
                retry_count = transaction.retry_count
            else:
                retry_count = 0
            return Response(
                {
                    "status": status_code, 
                    "retry_count": retry_count
                }, 200)

render_image_from_prompt = RenderImageFromPromptView.as_view()

class EstimateRenderPrice(APIView):
    def post(self, request):
        """Estimate render price in point units (1 point = render 1 image 512x512"""
        """
            @Args:
                - raw_prompt
                - render_template_id
                - see other args in veminhhoa.render_image.lib.stable_diffusion.render_image()
        """
        data = request.data
        raw_prompt = data['raw_prompt'] if 'raw_prompt' in data else None
        render_template_id = data['render_template_id'] if 'render_template_id' in data else None 
        transaction_id = data['transaction_id'] if 'transaction_id' in data else None

        if (not raw_prompt) or (not render_template_id):
            return Response("Missing raw_prompt or render_template_id", 400)
        
        price, status_code = RenderManager.estimate_render_price(raw_prompt, render_template_id, transaction_id, data)
        if price: 
            return Response(
                {
                    "status": status_code, 
                    "price": price
                }, 
                200
            )
        else:
            return Response(
                {
                    "status": status_code, 
                }, 200)

estimate_render_price = EstimateRenderPrice.as_view()

class RenderTemplateViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RenderTemplateSerializer
    queryset = RenderTemplate.objects.all()

class RenderTransactionViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return RenderTransaction.objects.filter(user=user).all().order_by('-pk')
    serializer_class = RenderTransactionSerializer

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.all() 

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AuthorSerializer
    def get_queryset(self):
        return Author.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()

class GetBestAuthorView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        best_authors = Author.objects.filter(books__orders__isnull=False).annotate(revenue = Sum('books__orders__price')).order_by('-revenue').values('pk', 'name', 'revenue')
        return Response(best_authors, 200)