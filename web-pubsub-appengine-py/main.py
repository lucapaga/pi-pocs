#!flask/bin/python
from flask import Flask, jsonify
import sys, os, argparse, time

from google.cloud import pubsub_v1


#global pubsub_client
#global runargs

pubsub_client = None
runargs = None

app = Flask(__name__)

app.config['PROJECT'] = os.environ['GCLOUD_PROJECT']
app.config['GCP_PUBSUB_TOPIC_COMMANDS'] =  os.environ['GCP_PUBSUB_TOPIC_COMMANDS']
app.config['GCP_PUBSUB_SUBSCRIPTION_COMMANDS'] = os.environ['GCP_PUBSUB_SUBSCRIPTION_COMMANDS']
app.config['GCP_PUBSUB_TOPIC_STATUS'] = os.environ['GCP_PUBSUB_TOPIC_STATUS']


@app.route('/')
def index():
    return "Up'n'Running!"


#@app.route('/pubsub/p/commands', methods=['POST'])
#def piall(pubsub_message):
#    publish_message(
#        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
#        pubsub_message,
#        pubsub_client)


@app.route('/piall/<led_state>')
def piall(led_state):
 print("GCP_PROJECT: '{}'  |  GCP_PUBSUB_TOPIC_COMMANDS: '{}'".format(app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS']))
 print("Publishing Message to PUB/SUB ...")
 if led_state.lower() == "on":
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"red","action":"light-on"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"green","action":"light-on"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"light-bulb","action":"light-on"}',
        pubsub_client)
 elif led_state.lower() == "off":
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"red","action":"light-off"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"green","action":"light-off"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"light-bulb","action":"light-off"}',
        pubsub_client)
 else:
    #print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"red","action":"light-off"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"green","action":"light-off"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"light-bulb","action":"light-off"}',
        pubsub_client)
 print("Message Published to PUB/SUB ...")
 return pistate(led_state, led_state, led_state)


@app.route('/pitoggle/all')
def pitoggle():
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"red","action":"toggle"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"green","action":"toggle"}',
        pubsub_client)
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{"led_color":"light-bulb","action":"toggle"}',
        pubsub_client)
    return pistate("UNK", "UNK", "UNK")


#@app.route('/pistate')
def pistate(red_led_state, green_led_state, light_bulb_state):
    return jsonify({'result': 'OK', 'io_slots': [
                    { 'position': 'green_led', 'state': { 'value': green_led_state}}
                    , { 'position': 'red_led', 'state': { 'value': red_led_state}}
                    , { 'position': 'light_bulb', 'state': { 'value': light_bulb_state}}]})



@app.route('/pi/<led_color>/<led_state>')
def pi(led_color, led_state):
    publish_message(
        app.config['PROJECT'], app.config['GCP_PUBSUB_TOPIC_COMMANDS'],
        '{{"led_color":"{}","action":"light-{}"}}'.format(led_color, led_state),
        pubsub_client)
    return jsonify({'result': 'OK', 'led': { 'color': led_color.lower(), 'state': { 'value': led_state, 'default': 'False'}}})


def publish_message(project, topic_name, message, client):
    print("Istantiating PUB/SUB client ...")
    publisher = pubsub_v1.PublisherClient()
    print("Client is '{}'".format(publisher))
    topic_path = publisher.topic_path(project, topic_name)
    print("TOPIC is '{}'".format(topic_path))

    data = u'{}'.format(message)
    print("MESSAGE DATA is '{}'".format(data))
    data = data.encode('utf-8')
    print("MESSAGE DATA UTF8 is '{}'".format(data))

    print("Publishing Message ...")
    publisher.publish(topic_path, data=data)
    print("Message Published!")


    #print('Published message: >{}<'.format(message))



if __name__ == '__main__':
    #pubsub_client=pubsub_v1.PublisherClient()
    app.run(debug=True, host='127.0.0.1', port=8080)
