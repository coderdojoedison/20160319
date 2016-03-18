import time
import RPi.GPIO as GPIO

def showColor(whichColor, howLong):
	print(str(whichColor) + " light is ON for " + str(howLong) + " seconds")
	GPIO.output(whichColor, True)
	time.sleep(howLong)
	GPIO.output(whichColor, False)

def glowGreen():
	showColor(GREEN, 7)
	
def glowRed():
	showColor(AMBER, 3)
	showColor(RED, 7)
	
# Assign GPIO pins to colors. 
# Change the numbers to actual pin number connected
GREEN = 11
RED = 7
AMBER = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(AMBER,GPIO.OUT)

glowGreen()
glowRed()
GPIO.cleanup()
