#!/bin/bash

#source ${HOME}/env/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS=${GCP_APP_CRED_JSON_PATH}

python 01_pubsub_gpiozero.py \
      --project ${GCP_PROJECT_NAME} \
      --commands_topic_name ${GCP_PUBSUB_TOPIC_COMMANDS} \
      --commands_subscription_name ${GCP_PUBSUB_SUBSCRIPTION_COMMANDS} \
      --status_topic_name ${GCP_PUBSUB_TOPIC_STATUS} \
      --emulate_gpio ${PI_EMULATE_GPIO}
