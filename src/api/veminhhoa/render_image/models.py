from django.db import models
from django.contrib.postgres.fields import ArrayField

class RenderTemplate(models.Model): 
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    prompt_template = models.TextField(blank=True)
    num_inference_steps = models.IntegerField(default=50)
    prompt_strength = models.FloatField(default=0.8)
    guidance_scale = models.FloatField(default=7.5)
    price = models.FloatField(default=1.0)
    improve_face = models.BooleanField(default=False)

    def get_id(self):
        return self.pk

    def process_prompt(self, raw_prompt):
        return self.prompt_template.format(raw_prompt)

from django.contrib.auth import get_user_model
User = get_user_model()

class RenderTransaction(models.Model):
    """This model save user render transactions"""
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    raw_prompt = models.TextField(blank=True)
    translated_prompt = models.TextField(blank=True)
    processed_prompt = models.TextField(blank=True)
    render_template = models.ForeignKey(RenderTemplate, null=True, on_delete=models.SET_NULL)
    image_urls = ArrayField(
        models.TextField(blank=True), 
        null=True
    )
    estimated_price = models.FloatField(default=0)
    final_price = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField(default=0)

    # retry count
    retry_count = models.IntegerField(default=5)

    # cashback program
    user_review = models.IntegerField(default=0)
    user_feedback = models.TextField(blank=True)