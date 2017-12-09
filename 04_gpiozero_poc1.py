from gpiozero import LED, Button
from time import sleep

green_led = LED(18)
red_led = LED(17)

green_led.on()
sleep(1)
red_led.on()

sleep(5)

red_led.off()
green_led.off()
