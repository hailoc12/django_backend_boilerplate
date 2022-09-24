from django.db import models

class RenderTemplate(models.Model): 
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    prompt_template = models.TextField(blank=True)
    num_inference_steps = models.IntegerField(default=0)
    prompt_strength = models.IntegerField(default=0)
    guidance_scale = models.IntegerField(default=0)

    def get_id(self):
        return self.pk