# Import the following modules
from PIL import Image
from pathlib import Path
import random

from captcha.image import ImageCaptcha
from random import randint

dir = "./captcha_images_test"

def generate_string(nb):
    chars = "2345678bcdefgmnpwxy"
    s = ""
    for i in range(nb):
        s += chars[randint(0, len(chars) - 1)]
    return s


def generate_captcha(s):
    # Create an image instance of the given size
    image = ImageCaptcha(width=200, height=50, fonts=["times.ttf", "arial.ttf"])

    # Image captcha text
    captcha_text = s

    # generate the image of the given text
    data = image.generate(captcha_text)

    # write the image on the given file and save it
    image.write(captcha_text, f'{dir}/{captcha_text}.png')


for i in range(32):
    generate_captcha(generate_string(5))

files = Path(f"{dir}/").glob('*.png')

for x in files:
    base = Image.open(x).convert('RGBA')
    base.save(x)

