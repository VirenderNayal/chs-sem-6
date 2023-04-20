from PIL import Image
image = Image.open('ss.png')

new_image = image.resize((28, 28))
new_image.save('new.png')