import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit('Too many command-lines arguments')
elif len(sys.argv) <3:
    sys.exit('Too few command-line arguments')
elif not sys.argv[1].lower().endswith(('.jpg', '.jpeg', '.png')):
    sys.exit('Invalid input')
elif not sys.argv[2].lower().endswith(('.jpg', '.jpeg', '.png')):
    sys.exit('Invalid output')
elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
    sys.exit('Input and output have different extensions')


def main():
   # Open the input and return the image
   input_image = open_image(sys.argv[1])
   # resize and crop the input with ImageOps.fit, per  using default values
   resized_image = resize_and_crop(input_image)
   # open overlayer and return de overlayer image
   overlayer_image = open_image('shirt.png')
   # overlay the shirt with Image.paste
   ovelayed_image = overlayer_images(resized_image, overlayer_image)
   # save the image
   ovelayed_image.Image.save(
       fp = sys.argv[2]
   )

def open_image(image: str):
    try:
        return Image.open(image)
    except FileNotFoundError:
        sys.exit('Input does not exist')

def resize_and_crop(image: Image):
    return ImageOps.fit(image, size=(600, 600))

def overlayer_images(image_backgound: Image, image_front: Image):
    image_backgound.Image.paste(im= image_front)
    return image_backgound