from PIL import Image

mask_image = Image.open('mask.png')
word_matrix_image = Image.open('word_matrix.png')
mask_image = mask_image.resize((500,500))
word_matrix_image = word_matrix_image.resize((500,500))

mask_image.putalpha(150)
word_matrix_image.putalpha(300)
word_matrix_image.paste(im=mask_image, box=(0,0), mask=mask_image)
word_matrix_image.show()