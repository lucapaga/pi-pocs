#!flask/bin/python
from flask import Flask, jsonify
import sys

from gpiozero import LED, Button
#from time import sleep

GREEN_LED_NR=18
RED_LED_NR=17
BUTTON_NR=23

@app.route('/')
def index():
    return "Up'n'Running!"


@app.route('/piall/<led_state>')
def piall(led_state):
 if led_state.lower() == "on":
  red_led.on()
  green_led.on()
 elif led_state.lower() == "off":
  red_led.off()
  green_led.off()
 else:
  print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
  red_led.off()
  green_led.off()
 return pistate()


@app.route('/pitoggle')
def pitoggle():
 red_led.toggle()
 green_led.toggle()
 return pistate()


@app.route('/pistate')
def pistate():
 return jsonify({'result': 'OK', 'io_slots': [
                    { 'position': GREEN_LED_NR, 'state': { 'value': green_led.is_lit}}
                    , { 'position': RED_LED_NR, 'state': { 'value': red_led.is_lit}}]})


@app.route('/piraw/<int:io_slot>/<led_state>')
def piraw(io_slot, led_state):
 gpio_channel=io_slot
 default_state=False

 theLED = None
 if(io_slot == GREEN_LED_NR):
     theLED = green_led
 else:
     theLED = red_led

 if led_state.lower() == "on":
  theLED.on()
 elif led_state.lower() == "off":
  theLED.off()
 else:
  print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
  theLED.off()
  default_state=True

 return jsonify({'result': 'OK', 'io_slot': { 'position': gpio_channel, 'state': { 'value': theLED.is_lit, 'default': default_state}}})


@app.route('/pi/<led_color>/<led_state>')
def pi(led_color, led_state):
 print "Processing LED '" + led_color + "' to STATE '" + led_state + "'"
 default_state=False

 theLED = None
 if led_color.lower() == "green":
  print "Operating GREEN LED ..."
  theLED = green_led
 elif led_color.lower() == "red":
  print "Operating RED LED ..."
  theLED = red_led
 else:
  print "Unknown color: " + led_color
  return jsonify({'result': 'KO', 'error':'Unknown LED color'})

 if led_state.lower() == "on":
  theLED.on()
 elif led_state.lower() == "off":
  theLED.off()
 else:
  print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
  theLED.off()
  default_state=True

 return jsonify({'result': 'OK', 'led': { 'color': led_color.lower(), 'state': { 'value': theLED.is_lit, 'default': default_state}}})



def on_button_pressed(button):
 print("Pulsante premuto!")
 if green_led.is_lit:
     print("LED is ON, switching OFF!")
     red_led.off()
     green_led.off()
     #bz.beep(on_time=.5, off_time=.2, n=3, background=False)
     #bz.beep()
     #sleep(1)
     #bz.beep()
 else:
     print("LED is OFF, switching ON!")
     green_led.on()
     red_led.on()
     #bz.beep()

green_led = LED(GREEN_LED_NR)
red_led = LED(RED_LED_NR)
button = Button(BUTTON_NR)
button.when_pressed = on_button_pressed

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
