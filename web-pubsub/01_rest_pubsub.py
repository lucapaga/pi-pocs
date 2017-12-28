#!flask/bin/python
from flask import Flask, jsonify
import sys

from google.cloud import pubsub_v1

@app.route('/')
def index():
    return "Up'n'Running!"

app = Flask(__name__)

pubsub_client = None
runargs = None

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
