from gpiozero import LED, Button, Buzzer
from time import sleep

def on_button_pressed(button):
 print("Pulsante premuto!")
 if green_led.is_lit:
     print("LED is ON, switching OFF!")
     red_led.off()
     green_led.off()
     bz.beep(on_time=.2, off_time=.1, n=3, background=False)
 else:
     print("LED is OFF, switching ON!")
     green_led.on()
     red_led.on()
     bz.beep(on_time=.2, off_time=.1, n=2, background=False)

green_led = LED(18)
red_led = LED(17)
bz = Buzzer(3)
button = Button(23)
button.when_pressed = on_button_pressed

while(True):
    i = 0

#green_led.on()
#sleep(1)
#red_led.on()
