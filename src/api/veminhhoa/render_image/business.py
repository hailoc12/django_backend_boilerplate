# Function: this module handle all render_image logics
from veminhhoa.render_image.lib.stable_diffusion import Stable_Diffusion

class RenderManager():
    """This class handles all logics relating to user renders"""
    @staticmethod
    def render_images_from_user_prompt(raw_prompt, render_template_id, options):
        """This handle render prompt to images"""
        """
            @Return: (a list of image urls, status_code)
        """
        translated_prompt = raw_prompt
        processed_prompt = translated_prompt

        options['prompt'] = processed_prompt

        image_urls, status_code = Stable_Diffusion.render_image(options)
        return image_urls, status_code

