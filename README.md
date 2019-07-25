# Free Port Riga

One app for all cargo-truck drivers.

>Book your ferry trips, track your trips in real time to avoid any delay or cancelled ferry trip, inform your forwarder about your truck route.

<div style="margin: auto; width: 90%;">
<img src="https://i.imgur.com/PV9ZF2K.png" width=30%/>
<img src="https://i.imgur.com/BumLyKH.png" width=30%/>
<img src="https://i.imgur.com/vQrrdYY.png" width=30%/>
</div>

Web app using Angular 8+.

You can:

* Book a ferry trip on a ferry line company
* Fill your CMR form
* Track your trips times (scheduled, estimated and real time)
* Create your truck route
* Check ferry lines schedules
* Keep your ferry trips and CMR forms history

<div style="margin: auto; width:90%;">
<img src="https://i.imgur.com/JePv57N.png" width=45%/>
<img src="https://i.imgur.com/R6VE8k9.png" width=45%/>
</div>

## Installation

* Install [node](https://nodejs.org/en/) (which includes `npm`)
* Install [Angular CLI](https://cli.angular.io/).

## Usage

* `npm install` in project's root directory
* `npm start` to run the dev server

* `ng build --prod` to build the production project
    * Website is built in directory `dist/freeport-riga/`

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Project's architecture

Angular components are in the `src/app/components/` directory.

Services are in the `src/app/services` directory.
Services are used to communicate with the backend part and retrieve data from it. (Trips, user login, etc.)

The `AuthGuard.ts` in the `src/app/guards/` directory is used to "protect" the project from unauthenticated users. They have to pass the guard (i.e. be logged in) to see the application.