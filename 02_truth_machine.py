import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

your_name = raw_input("Enter your name: ")
print "Your name is: " + your_name.lower()

if your_name.lower() == "chiara":
 print "Hi " + your_name + "!"
 GPIO.output(18, GPIO.HIGH)
 time.sleep(3)
 GPIO.output(18, GPIO.LOW)
else:
 print "No! You're not " + your_name + "..."
 GPIO.output(17, GPIO.HIGH)
 time.sleep(3)
 GPIO.output(17, GPIO.LOW)

print "This is it"
