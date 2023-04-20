import time
import pyscreenshot
from PIL import Image
import numpy as np
import pickle

# print("Draw...")

# time.sleep(1)

# print("Taking Screenshot...")
# pic = pyscreenshot.grab(bbox=(100, 250, 600, 600)) #left, 
# # pic.show()
# pic.save("ss.png")

# print("Converting image to array...")

# image = Image.open('ss.png')

# new_image = image.resize((28, 28))
# new_image.save('new.png')

img = Image.open('new.png').convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W

np_img[np_img < 15] = 0
np_img[np_img >= 15] = 1
print(np_img)

# np_img = np_img.flatten() # 2D to 1D

# pickled_model = pickle.load(open('test.pickle', 'rb'))
# pred_arr = pickled_model.predict(np_img)

# with open('test.pickle', 'rb') as f:
#     model = pickle.load(f)

# pred_arr = model.predict(np_img)

# print("Maybe you have drawn :")
# print(pred_arr.argmax())
# print("\n With ", pred_arr.max(), "% accuracy.")