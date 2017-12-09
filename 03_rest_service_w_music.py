#!flask/bin/python
from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time
import sys


BuzzerPin = 3

CL = [0, 131, 147, 165, 175, 196, 211, 248] # Low C Note Frequency
CM = [0, 262, 294, 330, 350, 393, 441, 495] # Middle C Note Frequency
CH = [0, 525, 589, 661, 700, 786, 882, 990] # High C Note Frequency

song_1 = [ CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6], # Sound Notes 1
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5] ]

beat_1 = [ 1, 1, 3, 1, 1, 3, 1, 1, # Beats of song 1, 1 means 1/8 beats
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3 ]

song_2 = [ CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1], # Sound Notes 2
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1] ]

beat_2 = [ 1, 1, 2, 2, 1, 1, 2, 2, # Beats of song 2, 1 means 1/8 beats
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3 ]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(BuzzerPin, GPIO.OUT) # Set pins' mode is output




app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/pi/play-music')
def pi_sound():

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
