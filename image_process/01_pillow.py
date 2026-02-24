from PIL import Image

first_image = Image.open('image_1.jpg')
# print(type(first_image)) # return <class 'PIL.JpegImagePlugin.JpegImageFile'>

# print(first_image) # return <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=339x509 at 0x105945FD0>
# first_image.show() # for show Image

# print(first_image.size) # Size of image
# print(first_image.filename) # file name 
# print(first_image.format_description)



# Croping the image
# in the image  X is forword y is downword
# y, x---------> (width)
# |
# |
# |
# v
# (height)

# (0,0)__________________________________(800,0)

#     |                |                |
#     |          top (upper)            |
#     |                v                |
#     |     left --> [Rect] <-- right   |
#     |                ^                |
#     |            bottom (lower)       |
#     |_________________________________|
# (0,600)                               (800,600)

# first_image.crop((LEFT,UPPER,RIGHT,LOWER))
# left, upper -> These define the starting point (the top-left corner of your cut).
# right, lower -> They are the ending coordinates on the original image's grid.
# crop_image = first_image.crop((0,0,400,610))
# crop_image.show()
# first_image.show()

pencil_image = Image.open('pencils.jpg')
# print(pencil_image.size) #(2183, 1228)
# height = 1228/2
width = 2183/5
# print(pencil_image.height)
# print(pencil_image.width)

crop_pencil_image = pencil_image.crop((0,1000,width, 1228))
# pencil_image.show()
# crop_pencil_image.show()

# first_image.paste(im=crop_pencil_image, box=(0,0))
# first_image.show()

resize_pencil_image = pencil_image.resize((200,200))
# resize_pencil_image.show()

rotate_image = resize_pencil_image.rotate(180)
rotate_image.show()