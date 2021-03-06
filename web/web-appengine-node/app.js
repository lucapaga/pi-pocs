/**
 * Copyright 2016, Google, Inc.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// [START app]
'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const Buffer = require('safe-buffer').Buffer;
const process = require('process'); // Required for mocking environment variables

// By default, the client will authenticate using the service account file
// specified by the GOOGLE_APPLICATION_CREDENTIALS environment variable and use
// the project specified by the GCLOUD_PROJECT environment variable. See
// https://googlecloudplatform.github.io/gcloud-node/#/docs/google-cloud/latest/guides/authentication
// These environment variables are set automatically on Google App Engine
const PubSub = require('@google-cloud/pubsub');

// Instantiate a pubsub client
const pubsub = PubSub();

const app = express();

//app.set('view engine', 'pug');
//app.set('views', path.join(__dirname, 'views'));

const formBodyParser = bodyParser.urlencoded({ extended: false });
const jsonBodyParser = bodyParser.json();

// List of all messages received by this instance
const messages = [];

// The following environment variables are set by app.yaml when running on GAE,
// but will need to be manually set when running locally.
//const PUBSUB_VERIFICATION_TOKEN = process.env.PUBSUB_VERIFICATION_TOKEN;

const topic = pubsub.topic(process.env.GCP_PUBSUB_TOPIC_COMMANDS);

app.use(express.static('static'))

// [START index]
app.get('/', (req, res) => {
  //res.render('index', { messages: messages });
  res.status(200).send('Ready to go');
});

app.get('/piall/:ledState', (req, res) => {
  const led_state=req.params["ledState"];
  var action="light-"

  if(led_state == "on") {
    action = action + led_state
  } else if(led_state == "off") {
    action = action + led_state
  } else {
    action = action + "off"
  }
  console.log("Moving all LEDs/Bulbs to '" + action + "'")

  topic.publish({
      data: '{"led_color":"red","action":"' + action + '"}'
    }, (err) => {
      if (err) {
        console.warn("Unable to send message (RED LED): ", err);
        return;
      }
      console.log("Message sent: RED LED");
    });
  topic.publish({
      data: '{"led_color":"green","action":"' + action + '"}'
    }, (err) => {
      if (err) {
        console.warn("Unable to send message (GREEN LED): ", err);
        return;
      }
      console.log("Message sent: GREEN LED");
    });
  topic.publish({
      data: '{"led_color":"light-bulb","action":"' + action + '"}'
    }, (err) => {
      if (err) {
        console.warn("Unable to send message (LIGHT BULB): ", err);
        return;
      }
      console.log("Message sent: LIGHT BULB");
    });

  res.status(200).send('All messages sent');
})

app.post('/', formBodyParser, (req, res, next) => {
  if (!req.body.payload) {
    res.status(400).send('Missing payload');
    return;
  }

  topic.publish({
    data: req.body.payload
  }, (err) => {
    if (err) {
      next(err);
      return;
    }
    res.status(200).send('Message sent');
  });
});
// [END index]

// [START push]
app.post('/pubsub/push', jsonBodyParser, (req, res) => {
  if (req.query.token !== PUBSUB_VERIFICATION_TOKEN) {
    res.status(400).send();
    return;
  }

  // The message is a unicode string encoded in base64.
  const message = Buffer.from(req.body.message.data, 'base64').toString('utf-8');

  messages.push(message);

  res.status(200).send();
});
// [END push]

// Start the server
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
  console.log('Press Ctrl+C to quit.');
});
// [END app]

module.exports = app;
