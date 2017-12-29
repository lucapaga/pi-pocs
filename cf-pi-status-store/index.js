'use strict';

/*
*     {
*         'position': 'green_led',
*         'state': {
*             'value': green_led_state
*         }
*     }
*/
exports.saveLedStatus = function saveLedStatus (req, res) {
  console.log(`Handling message: '${req.body}'`);

  const Datastore = require('@google-cloud/datastore');
  const uuid = require('uuid');

  var datastore = Datastore({
    projectId: "luca-paganelli-formazione"
  });

  var kind = 'LedStatus';

  var greenLedName = req.body.position;//'green_led';// + uuid.v4();
  var greenLedState = req.body.state.value;//'green_led';// + uuid.v4();

  console.log(`LED: '${greenLedName}' - STATE: '${greenLedState}'`);

  var greenLedKey = datastore.key([kind, greenLedName]);
  var greenLedEntity = {
    key: greenLedKey,
    data: {
      led_state: greenLedState
    }
  };

  datastore.save(greenLedEntity)
    .then(() => {
      console.log(`Saved '${greenLedEntity.key.name}': '${greenLedEntity.data.led_state}'`);
    })
    .catch((err) => {
      console.error('ERROR:', err);
    });

  res.send('Got it!');
};
// Saves the entity
