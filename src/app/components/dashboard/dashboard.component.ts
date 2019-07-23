import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  bookATrip(): void {
    window.open('https://www.stenalinetravel.com/ferry-to-scandinavia', '_blank');
  }
}
