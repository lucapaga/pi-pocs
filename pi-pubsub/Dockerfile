FROM resin/raspberrypi3-python:2.7-slim

MAINTAINER luca.paga@gmail.com

RUN pip install --upgrade gpiozero && \
    pip install --upgrade google-cloud-pubsub \
    mkdir -p /opt/pi-pocs

WORKDIR /opt/pi-pocs

COPY ./08_rest_gpiozero.py /opt/pi-pocs/

EXPOSE 5000
CMD ["python", "./08_rest_gpiozero.py"]
