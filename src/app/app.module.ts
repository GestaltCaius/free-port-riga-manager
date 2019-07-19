import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { LoginComponent } from './components/login/login.component';
import { AuthService } from './services/auth.service';
import { HttpClientModule } from '@angular/common/http';
import { CurrentTripComponent } from './components/current-trip/current-trip.component';
import { SearchTripComponent } from './components/search-trip/search-trip.component';
import { TripHistoryComponent } from './components/trip-history/trip-history.component';
import { BookTripComponent } from './components/book-trip/book-trip.component';
import { CmrFormComponent } from './components/cmr-form/cmr-form.component';
import { TabComponent } from './components/tab/tab.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    LoginComponent,
    CurrentTripComponent,
    SearchTripComponent,
    TripHistoryComponent,
    BookTripComponent,
    CmrFormComponent,
    TabComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
