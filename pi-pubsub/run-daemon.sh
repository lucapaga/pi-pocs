#!/bin/bash

source ${HOME}/env/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/sa/pi-pocs-pubsub-sa01-00afc7e81369.json

python 01_pubsub_gpiozero.py \
      --project luca-paganelli-formazione \
      --commands_topic_name gpio_commands_topic \
      --commands_subscription_name gpio_commands_subscription \
      --status_topic_name gpio_status_topic
