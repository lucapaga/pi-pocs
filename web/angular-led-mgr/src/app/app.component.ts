import { Component, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { MatButtonToggleChange } from '@angular/material/button-toggle';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent { // implements OnInit {
  title = 'Pi LED Manager';

  constructor(private http: HttpClient) {}

  toggleRedLED(theEvent : MatButtonToggleChange) {
    console.log("Spiking command:", theEvent);

    if(theEvent.source.checked) {
      this.http.get('/pi/red/on').subscribe(data => {
        // Read the result field from the JSON response.
        //this.results = data['results'];
        console.log("That's it: ", data);
      });
    } else {
      this.http.get('/pi/red/off').subscribe(data => {
        // Read the result field from the JSON response.
        //this.results = data['results'];
        console.log("That's it: ", data);
      });
    }

  }

  toggleGreenLED(theEvent : MatButtonToggleChange) {
    console.log("Spiking command:", theEvent);

    if(theEvent.source.checked) {
      this.http.get('/pi/green/on').subscribe(data => {
        // Read the result field from the JSON response.
        //this.results = data['results'];
        console.log("That's it: ", data);
      });
    } else {
      this.http.get('/pi/green/off').subscribe(data => {
        // Read the result field from the JSON response.
        //this.results = data['results'];
        console.log("That's it: ", data);
      });
    }

  }
}
