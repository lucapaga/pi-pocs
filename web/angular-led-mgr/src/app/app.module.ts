import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatButtonModule, MatCheckboxModule, MatToolbarModule } from '@angular/material';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatSidenavModule } from '@angular/material/sidenav';

import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule, HttpClientModule,
    MatButtonModule, MatCheckboxModule,
    MatButtonToggleModule, MatIconModule,
    MatSidenavModule, MatToolbarModule
  ],
  exports: [
    MatButtonModule, MatCheckboxModule,
    MatButtonToggleModule, MatIconModule,
    MatSidenavModule, MatToolbarModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
