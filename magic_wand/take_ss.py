import pyscreenshot
pic = pyscreenshot.grab(bbox=(100, 250, 600, 600)) #left, 
pic.show()
pic.save("ss.png")