from veminhhoa.render_image.lib.stable_diffusion import Stable_Diffusion
import random
import os 
from pathlib import Path

ROOT_DIR = str(Path(__file__).resolve(strict=True).parent.parent.parent)

# def test_stable_diffusion_lib():
#     options = {
#         'prompt': 'multicolor hyperspace', 
#     }
#     filename = str(random.randint(0, 32767)) + '.jpg'
#     model = Stable_Diffusion
#     path = ROOT_DIR + '/export'
#     model.render_image_and_save(options, path=path, filenames=[filename])
#     assert(os.path.exists(path + '/' + filename) == True)
