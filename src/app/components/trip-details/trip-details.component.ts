import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-trip-details',
  templateUrl: './trip-details.component.html',
  styleUrls: ['./trip-details.component.css']
})
export class TripDetailsComponent implements OnInit {

  showCMR = false;

  constructor() { }

  ngOnInit() {
  }

  editCMR(): void {
    this.showCMR = true;
  }

}
