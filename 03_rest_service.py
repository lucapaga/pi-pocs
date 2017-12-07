#!flask/bin/python
from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/pi/<led_color>/<led_state>')
def pi(led_color, led_state):
 print "Processing LED '" + led_color + "' to STATE '" + led_state + "'"
 gpio_channel=0
 gpio_target_state=GPIO.LOW
 target_state='off'
 default_state=False

 if led_state.lower() == "on":
  gpio_target_state=GPIO.HIGH
  target_state='on'
 elif led_state.lower() == "off":
  gpio_target_state=GPIO.LOW
 else:
  print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
  default_state=True

 if led_color.lower() == "green":
  print "Operating GREEN LED ..."
  gpio_channel=18
  operate_gpio(gpio_channel, gpio_target_state)
  return jsonify({'result': 'OK', 'led': { 'color': 'green', 'state': { 'value': target_state, 'default': default_state}}})
 elif led_color.lower() == "red":
  print "Operating RED LED ..."
  gpio_channel=17
  operate_gpio(gpio_channel, gpio_target_state)
  #return jsonify({'result': True})
  return jsonify({'result': 'OK', 'led': { 'color': 'red', 'state': { 'value': target_state, 'default': default_state}}})
 else:
  print "Unknown color: " + led_color
  return jsonify({'result': 'KO', 'error':'Unknown LED color'})

def operate_gpio(channel, state):
 GPIO.output(channel, state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

