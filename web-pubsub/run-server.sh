#!/bin/bash

#source ${HOME}/env/bin/activate
echo "Setting up security using '${GCP_APP_CRED_JSON_PATH}' ..."
export GOOGLE_APPLICATION_CREDENTIALS=${GCP_APP_CRED_JSON_PATH}


echo "Running daemon ... "
echo " - GCP Project:     ${GCP_PROJECT_NAME}"
echo " - COMMANDS:"
echo "     - TOPIC:       ${GCP_PUBSUB_TOPIC_COMMANDS}"
echo " - STAUS:"
echo "     - TOPIC:       ${GCP_PUBSUB_TOPIC_STATUS}"
echo ""
echo ""

python 08_rest_pubsub.py \
        --project ${GCP_PROJECT_NAME} \
        --commands_topic_name ${GCP_PUBSUB_TOPIC_COMMANDS}
#        --status_topic_name ${GCP_PUBSUB_TOPIC_STATUS}

echo "DONE!"
echo "Exiting ..."
