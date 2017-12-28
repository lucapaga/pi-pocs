#!flask/bin/python
from flask import Flask, jsonify
import sys, os, argparse, time

from google.cloud import pubsub_v1


#global pubsub_client
#global runargs

pubsub_client = None
runargs = None
app = Flask(__name__)


@app.route('/')
def index():
    return "Up'n'Running!"


@app.route('/piall/<led_state>')
def piall(led_state):
 if led_state.lower() == "on":
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"red","action":"light-on"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"green","action":"light-on"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"light-bulb","action":"light-on"}',
        pubsub_client)
 elif led_state.lower() == "off":
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"red","action":"light-off"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"green","action":"light-off"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"light-bulb","action":"light-off"}',
        pubsub_client)
 else:
    print "Unknown LED STATE (" + led_state + "), defaulting to OFF"
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"red","action":"light-off"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"green","action":"light-off"}',
        pubsub_client)
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"light-bulb","action":"light-off"}',
        pubsub_client)
 return pistate(led_state, led_state, led_state)


@app.route('/pitoggle/all')
def pitoggle():
 #red_led.toggle()
 #green_led.toggle()
 return pistate("UNK", "UNK", "UNK")


#@app.route('/pistate')
def pistate(red_led_state, green_led_state, light_bulb_state):
    return jsonify({'result': 'OK', 'io_slots': [
                    { 'position': GREEN_LED_NR, 'state': { 'value': green_led_state}}
                    , { 'position': RED_LED_NR, 'state': { 'value': red_led_state}}]})



@app.route('/pi/<led_color>/<led_state>')
def pi(led_color, led_state):
    publish_message(runargs.project, runargs.commands_topic_name,
        '{"led_color":"{}","action":"light-{}"}'.format(led_color, led_state),
        pubsub_client)
    return jsonify({'result': 'OK', 'led': { 'color': led_color.lower(), 'state': { 'value': led_state, 'default': 'False'}}})


def publish_message(project, topic_name, message, client):
    publisher = client #pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic_name)

    data = u'{}'.format(message)
    data = data.encode('utf-8')
    publisher.publish(topic_path, data=data)

    print('Published messages.')






if __name__ == '__main__':
    global pubsub_client
    global runargs

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
            '--project',
            default=os.environ.get('GOOGLE_CLOUD_PROJECT'),
            help='GCP cloud project name')
    parser.add_argument(
            '--commands_topic_name',
            required=True,
            help='PUB/SUB TOPIC for COMMANDS')

    runargs=parser.parse_args()
    pubsub_client=pubsub_v1.PublisherClient()
    app.run(debug=True, host='0.0.0.0')
