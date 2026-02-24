# Color Transparancy
# RGBA = Red, Green, Blue, Alpha

from PIL import Image

red_image = Image.open('red.avif')
blue_image = Image.open('blue.avif')
green_image = Image.open('green.png')

# red_image.putalpha(100)
# green_image.putalpha(100)
# blue_image.putalpha(100)

red_image = red_image.resize((200,200))
green_image = green_image.resize((200,200))
blue_image = blue_image.resize((200,200))

red_image.putalpha(100)
green_image.putalpha(100)
blue_image.putalpha(100)

blue_image.paste(im=red_image, box=(0,0), mask=red_image)

blue_image.save('purple.png')
