import { Component, OnInit } from '@angular/core';

declare var $: any; // Use JQuery, imported in index.html through bootstrap's CDN

@Component({
  selector: 'app-book-trip',
  templateUrl: './book-trip.component.html',
  styleUrls: ['./book-trip.component.css']
})
export class BookTripComponent implements OnInit {

  haveBookedATrip = false;

  constructor() { }

  ngOnInit() {
    $("#modal").modal('show');
  }

  showForm(): void {
    this.haveBookedATrip = true;
  }
}
