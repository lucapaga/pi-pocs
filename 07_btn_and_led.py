from gpiozero import LED, Button
from time import sleep

def on_button_pressed(button):
 print("Pulsante premuto!")
 if green_led.is_lit:
     print("LED is ON, switching OFF!")
     red_led.off()
     green_led.off()
 else:
     print("LED is OFF, switching ON!")
     green_led.on()
     red_led.on()

green_led = LED(18)
red_led = LED(17)

button = Button(23)
button.when_pressed = on_button_pressed

while(True):
    i = 0

#green_led.on()
#sleep(1)
#red_led.on()
