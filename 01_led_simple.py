import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

for i in range(0, 10):
 print "Led ON the " + str(i) + "th time"
 GPIO.output(18, GPIO.HIGH)
 time.sleep(1)
 print "Switching LED off the " + str(i) + "th time"
 GPIO.output(18, GPIO.LOW)
 time.sleep(2)

print "This is it"
