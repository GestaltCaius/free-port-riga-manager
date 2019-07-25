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
import { AuthGuard } from './guards/auth.guard';
import { CmrFormComponent } from './components/cmr-form/cmr-form.component';


const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full', canActivate: [AuthGuard]},
  { path: 'login', component: LoginComponent, canActivate: [AuthGuard]},
  { path: 'home', component: DashboardComponent, canActivate: [AuthGuard]},
  { path: 'tab', component: TabComponent, canActivate: [AuthGuard], children:
    [
      {path: 'current-trip', component: CurrentTripComponent, canActivate: [AuthGuard]},
      {path: 'search-trip', component: SearchTripComponent, canActivate: [AuthGuard]},
      {path: 'trip-history', component: TripHistoryComponent, canActivate: [AuthGuard]},
      {path: 'book-trip', component: BookTripComponent, canActivate: [AuthGuard]},
      {path: 'details', component: TripDetailsComponent, canActivate: [AuthGuard]},
      {path: 'crm-form', component: CmrFormComponent, canActivate: [AuthGuard]},
    ]
    }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
