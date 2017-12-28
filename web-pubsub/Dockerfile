FROM resin/raspberrypi3-python:2.7-slim

MAINTAINER luca.paga@gmail.com

RUN apt-get update && \
    apt-get install build-essential && \
    pip install --upgrade google-cloud && \
    pip install --upgrade google-cloud-pubsub && \
    pip install --upgrade Flask && \
    pip install --upgrade jsonify && \
    mkdir -p /opt/pi-pocs/static

WORKDIR /opt/pi-pocs

ENV GCP_APP_CRED_JSON_PATH=/opt/pi-pocs/pi-pocs-pubsub-sa01-00afc7e81369.json  \
    GCP_PROJECT_NAME=luca-paganelli-formazione                                 \
    GCP_PUBSUB_TOPIC_COMMANDS=gpio_commands_topic                              \
    GCP_PUBSUB_SUBSCRIPTION_COMMANDS=gpio_commands_subscription                \
    GCP_PUBSUB_TOPIC_STATUS=gpio_status_topic

COPY ./08_rest_pubsub.py /opt/pi-pocs/
COPY ./sa/pi-pocs-pubsub-sa01-00afc7e81369.json /opt/pi-pocs/
COPY ./run-server.sh  /opt/pi-pocs/
COPY ./run-daemon-on-docker-off-pi.sh  /opt/pi-pocs/

#COPY ./static/* /opt/pi-pocs/static/

EXPOSE 8080
CMD ["./run-daemon-on-docker-off-pi.sh"]
