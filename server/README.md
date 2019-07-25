# Cargo Driver Server

## Overview

You can find in this folder all the files needed to run the server application used by the Cargo Driver App. It implements a RESTful API to authenticate, access and edit data related to cargo drivers and forwarders.

## Caution

This server was made for demonstration purposes only! Under no circumstances must this server be used in a production environment as it is:

* Flask's built-in server (launched with `run.py`) must not be used. You should rely on other solutions such as nginx and uWSGI to serve the app.

* Communication between the front-end and this server must be secured with HTTPS: credentials and access tokens are transmitted in plaintext and therefore may be easily intercepted with a MITM attack.

* The app relies on an SQLite database to store persistant information. You may prefer to use a more reliable and more efficient DBMS such as PostreSQL or Microsoft SQL Server.

## Usage

You can send the following requests to the server:

* `POST /login` with `email` and `password` passwords, returns `access_token` and `refresh_token`
* `POST /logout/access` with `access_token` in request header
* `POST /logout/refresh` with `refresh_token` in request header
* `GET  /user/profile` with `access_token` in request header, returns user information
* `GET  /user/isloggedin` with `access_token` in request header, tells whether the user is connected or not
* `GET  /token/refresh` with `refresh_token` in request header, returns a new `access_token`

## Installation

* Install Python +3.5 (app was tested on Python 3.7.2)
* Create a virtual environment: `python3 -m venv .env`
* Activate it: `source .env/bin/activate` on Linux, `.env/Script/activate` on Windows
* Confgure the server by editing `config.py`
* Run the server: `python run.py`

Caution: To use flask commands, you must activate the newly created python environment.

## Database setup

You can already find an `app.db` database with some users stored in it.

If you want to reiniitialize the database, you can delete `app.db` and `migrations` directory. Then to recreate the database:

* `flask db init`: create a migration folder
* `flask db migrate`: create a migration using `models.py` to create tables
* `flask db upgrate`: create or update the SQLite database file `app.db`

To insert back demo entries to the database, execute `python init-db.py`

## Project's architecture

* `requirements.txt`: holds all python dependencies needed for this server application
* `run.py`: runs flask's built-in server, must be used for development and debugging purposes only
* `init-db.py`: inserts demo entries into the database
* `config.py`: defines server's configuration
* `app.db`: SQLite database with 3 user entries
* `app/models.py`: describes database tables
* `app/resources.py`: describes API resources/routes
* `app/__init__.py`: initializes Flask application, database and API resources
