# Function: this module is for calling stable_duffion APIs
from pathlib import Path
import environ
import replicate
from replicate.exceptions import ModelError
import random
import requests

class Stable_Diffusion():
    @staticmethod
    def render_image(options):
        """Render images from options"""
        """
            @Return: (a list of image urls hosted on replicate, status_code)

            Status_code: 
                0: ok 
                1: NSFW
                2: size is too large
        """

        prompt = options['prompt']
        width = options['width'] if 'width' in options else 512 
        height = options['height'] if 'height' in options else 512

        if (width >= 1024 and height > 768) or (height >=1027 and width > 768): # size is too large
            return [], 2

        init_image = options['init_image'] if 'init_image' in options else None
        mask = options['mask'] if 'mask' in options else None 
        prompt_strength = options['prompt_strength'] if 'prompt_strength' in options else 0.7 
        num_outputs = options['num_outputs'] if 'num_outputs' in options else 1 
        num_inference_steps = options['num_inference_steps'] if 'num_inference_steps' in options else 50 
        guidance_scale = options['guidance_scale'] if 'guidance_scale' in options else 7.5 
        seed = options['seed'] if 'seed' in options else 1

        model = replicate.models.get("stability-ai/stable-diffusion")

        # see more at: https://replicate.com/stability-ai/stable-diffusion
        try: 
            output = model.predict(
                prompt=prompt, 
                width=width, 
                height=height,
                # init_image=init_image,
                # mask=mask, 
                # prompt_strength=prompt_strength, 
                num_outputs=num_outputs, 
                num_inference_steps=num_inference_steps, 
                guidance_scale=guidance_scale, 
                seed = options['seed'] if 'seed' in options else random.randint(0, 32767)
            )
            return output, 0
        except ModelError:
            print("NSFW content detected")
            return [], 1
        
    @staticmethod
    def render_image_and_save(options, path, filenames=[]):
        num_outputs = options['num_outputs'] if 'num_outputs' in options else 1 
        output, status_code = Stable_Diffusion.render_image(options)

        if status_code == 0: 
            for i in range(0, num_outputs):
                with open(path + '/' + filenames[i], 'wb') as file:
                    result = requests.get(output[i], timeout=30)
                    if result.status_code == 200:
                        file.write(result.content)
                    else:
                        print(f"Can't get image from {output[i]}")

        return output, status_code
