# Cargo Driver App Backend - README

## Overview

You can find in this folder all the files needed to run the server application used by the Cargo Driver App. It implements a RESTful API to authenticate, access and edit data related to cargo drivers and forwarders.

## Caution

This server was made for demonstration purposes only! Under no circumstances must this server be used in a production environment as it is:

* Flask's built-in server (launched with `run.py`) must not be used. You should rely on other solutions such as nginx and uWSGI to serve the app.

* Communication between the front-end and this server must be secured with HTTPS: credentials and access tokens are transmitted in plaintext and therefore may be easily intercepted with a MITM attack.

* The app relies on an SQLite database to store persistant information. You may prefer to use a more reliable and more efficient DBMS such as PostreSQL or Microsoft SQL Server.

## Dependencies

This server relies on Python and some modules such as Flask to provide a RESTful API.

## Deployment

* Install Python +3.5
* Create a virtual environment: `python3 -m venv .env`
* Activate it: `source .env/bin/activate` on Linux, `.env/Script/activate` on Windows

## Files

* `requirements.txt`: holds all python dependencies needed for this server application
* `run.py`: runs flask's built-in server, must be used for development and debugging purposes only
* `init-db.py`: inserts demo entries into the database
* `config.py`: defines the server's configuration
