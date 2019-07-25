# Free Port Riga

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