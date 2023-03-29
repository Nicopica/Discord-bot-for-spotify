from PIL import Image, ImageDraw, ImageFont
import os
from get_path import IMAGE_BACKGROUND_PATH, FONT_PATH, IMAGE_GENRE_PATH

FONT = 'Cinzel-Regular.ttf'  # Download and place new font in discord_bot/fonts to change


def generate_image(text, color=None):  # Change color of font
    img = Image.open(IMAGE_BACKGROUND_PATH)
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.join(FONT_PATH, FONT), 40)
    d1.text((0, 5), text, fill=(200, 255, 255), font=font)
    img.save(IMAGE_GENRE_PATH)
    return IMAGE_GENRE_PATH

# 200, 255, 255
