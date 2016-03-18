import RPi.GPIO as GPIO
import time
GREEN_SIGNAL = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_SIGNAL,GPIO.OUT)
for x in range(0,3):
	GPIO.output(GREEN_SIGNAL,True)
	print "LED on"
	time.sleep(3)
	GPIO.output(GREEN_SIGNAL,False)
	print "LED off"
	time.sleep(3)
GPIO.cleanup()
