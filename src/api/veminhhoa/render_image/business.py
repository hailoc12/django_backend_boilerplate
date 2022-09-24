# Function: this module handle all render_image logics
from veminhhoa.render_image.lib.stable_diffusion import Stable_Diffusion
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction
from veminhhoa.render_image.lib.google_translation import PromptTranslation
from django.conf import settings 

class RenderManager():
    """This class handles all logics relating to user renders"""
    @staticmethod
    def render_images_from_user_prompt(user, raw_prompt, render_template_id, transaction_id, options):
        """This handle render prompt to images"""
        """
            @Return: (a list of image urls, status_code)
            see more status_code at veminhhoa.render_image.lib.stable_diffusion.render_image()
        """
        # translate prompt from vietnamese into english 
        translated_prompt = PromptTranslation.translate_prompt(raw_prompt)

        # apply template processing
        render_template = RenderTemplate.objects.filter(pk=render_template_id).first()
        if not render_template: 
            return image_urls, 3, None # wrong template id 
        processed_prompt = render_template.process_prompt(translated_prompt)

        # create transaction
        transaction = None 
        if not transaction_id:
            # create new transaction
            transaction = RenderTransaction.objects.create(
                raw_prompt = raw_prompt, 
                translated_prompt = translated_prompt, 
                processed_prompt = processed_prompt, 
                retry_count = settings.RENDER_RETRY_COUNT, 
                render_template = render_template
            )
        else:
            transaction = RenderTransaction.objects.filter(pk=transaction_id).first()
            if not transaction:
                status_code = 3
                return [], status_code, None
            
            if transaction.retry_count == 0:
                status_code = 5
                return [], status_code, transaction 

        # check if user have enough money
        estimated_price, status_code = RenderManager.estimate_render_price(raw_prompt, render_template_id, transaction_id, options) 

        if status_code != 0:
            return [], status_code, transaction
        
        transaction.estimated_price = estimated_price

        image_urls, status_code, final_price = Stable_Diffusion.render_image(options, processed_prompt, render_template)
        if status_code == 0: 
            transaction.final_price = final_price
            transaction.image_urls = image_urls
            transaction.retry_count = transaction.retry_count - 1
        
        transaction.status_code = status_code
        transaction.save()

        return image_urls, status_code, transaction

    @staticmethod
    def estimate_render_price(raw_prompt, render_template_id, transaction_id, options):
        """This function estimate render price based on render options"""
        """
            @Return: (a list of image urls, status_code)
            see more status_code at veminhhoa.render_image.lib.stable_diffusion.render_image()
        """
        translated_prompt = raw_prompt
        render_template = RenderTemplate.objects.filter(pk=render_template_id).first()
        if not render_template: 
            return None

        options['prompt'] = render_template.process_prompt(translated_prompt)

        price, status_code = Stable_Diffusion.estimate_render_price(options)
        return price, status_code

