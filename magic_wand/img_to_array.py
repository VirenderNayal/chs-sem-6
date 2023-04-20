from PIL import Image
import numpy as np
import pickle

img = Image.open('new.png').convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W



np_img[np_img < 15] = 0
np_img[np_img > 15] = 1

print(np_img)

np_img = np_img.flatten() # 2D to 1D


# print(np_img)


pickled_model = pickle.load(open('model.pkl', 'rb'))
print(pickled_model.predict(np_img))
