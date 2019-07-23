import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TabComponent } from './components/tab/tab.component';
import { CurrentTripComponent } from './components/current-trip/current-trip.component';
import { SearchTripComponent } from './components/search-trip/search-trip.component';
import { TripHistoryComponent } from './components/trip-history/trip-history.component';
import { BookTripComponent } from './components/book-trip/book-trip.component';
import { TripDetailsComponent } from './components/trip-details/trip-details.component';


const routes: Routes = [
  { path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {path: 'login', component: LoginComponent},
  {path: 'home', component: DashboardComponent},
  {
    path: 'tab', component: TabComponent, children:
    [
      {path: 'current-trip', component: CurrentTripComponent},
      {path: 'search-trip', component: SearchTripComponent},
      {path: 'trip-history', component: TripHistoryComponent},
      {path: 'book-trip', component: BookTripComponent},
      {path: 'details', component: TripDetailsComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
