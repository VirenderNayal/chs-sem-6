import  sys
import time 
import serial
import pyautogui

ArduinoSerial=serial.Serial('/dev/ttyUSB2',9600)  #Specify the correct COM port
pyautogui.FAILSAFE = False
time.sleep(1)                             #delay of 1 second

tx = 650
ty = 350
px = 0
py = 0
while True:
	try:
		data=str(ArduinoSerial.readline().decode('ascii'))   #read the data
		(x,y)=data.split(":")           # assigns to x,y and z
		(x,y)=float(x),float(y)                   #convert to int
		tx = tx+x-px
		ty = ty+y-py
		px = x
		py = y
		pyautogui.moveTo(tx, ty)          #move cursor to desired position from centre of screen
	except:
		print("ERROR!!!!")
