import time

# Assign GPIO pins to colors. 
# Change the numbers to actual pin number connected
GREEN = 13
RED = 6
AMBER = 7

def showColor(whichColor, howLong):
	print(str(whichColor) + " light is ON for " + str(howLong) + " seconds")
	time.sleep(howLong)

def glowGreen():
	showColor(GREEN, 7)
	
def glowRed():
	showColor(AMBER, 3)
	showColor(RED, 7)
	
glowGreen()
glowRed()
