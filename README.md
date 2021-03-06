# Maintenance tracker

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/db6a65a8b65c49ccb10d444f9ab9d848)](https://app.codacy.com/app/lawrenceChege/Pro-Tracker-v1?utm_source=github.com&utm_medium=referral&utm_content=lawrenceChege/Pro-Tracker-v1&utm_campaign=badger)
[![Coverage Status](https://coveralls.io/repos/github/lawrenceChege/Pro-Tracker-v1/badge.svg?branch=ft-157959190-api-views-requests)](https://coveralls.io/github/lawrenceChege/Pro-Tracker-v1?branch=ft-157959190-api-views-requests)
[![Build Status](https://travis-ci.org/lawrenceChege/Pro-Tracker-v1.svg?branch=ft-158094552-admin-endpoints)](https://travis-ci.org/lawrenceChege/Pro-Tracker-v1)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/59902067ff0a426aa825fbf06e71c4ef)](https://www.codacy.com/app/lawrenceChege/Pro-Tracker-v1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lawrenceChege/Pro-Tracker-v1&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/lawrenceChege/Pro-Tracker-v1/branch/develop/graph/badge.svg)](https://codecov.io/gh/lawrenceChege/Pro-Tracker-v1)

[![Build Status](https://travis-ci.org/lawrenceChege/Pro-Tracker-v1.svg?branch=ft-157959190-api-views-requests)](https://travis-ci.org/lawrenceChege/Pro-Tracker-v1)

## what it does

It provides the API endpoints for [maintenance tracker](https://pro-tracker.herokuapp.com)
> an app that manages maintenance and repair requests.

## Usage

* As a User, you can:
                    * Create an account
                    * Log in into the account
                    * Create a request
                    * View all your requests
                    * View a specific request
                    * View a specific category of requests
                    * View the status of a request
                    * Modify a request before it is approved
                    * delete a request before it is approved or after is has been resolved

* As an Admin, you can:
                    * Log into the admin account
                    * View all users requests
                    * View a user's request
                    * view a secific request
                    * View a specific category of requests
                    * View the status of a request
                    * Approve a request
                    * Reject a request
                    * Resolve a request

## Prerequisites

* Python 3.6 or later
* Git
* Virtualenv

## Installation

### Download option

* Go to [Pro-Tracker](https://github.com/lawrenceChege/Pro-Tracker-v1) on github
* Download the zip file and extract it
* Right click on the folder and open with terminal on linux or bash

>> we will continue from there :-)

** Cloning option **

* On your favorite terminal
* cd to where you want the repo to go
* Run the following command:

`git clone https://github.com/lawrenceChege/Pro-Tracker-v1.git`

* Then:

`cd Pro-Tracker`

## Virtual environment

> Now create a vitual environment, run:

`virtualenv env`

> or :

`python3 -m venv env`

> or any other that you know of.
> > Create a .env file and configure it with:

``` source env/bin/activate

export FLASK_APP="run.py"

export SECRET="thisissupposedtobeapassword"

export APP_SETTINGS="development"

export DATABASE_URL="postgresql:username@password    //localhost/Pro-Tracker" ```

>To activate virtualenv, run:

`source .env`

> or:

`source env/bin/activate`

**Install Dependencies**
> run:

`pip install -r requirements.txt`

> or:

`python3 -m pip install -r requirements.txt`

## API-Endpoints

For user:

Test | API-endpoint |HTTP-Verb
------------ | ------------- | ------------
Users can create new requests |/api/v1/requests/<user_id>/ | POST
users can view all their requests | /api/v1/requests/<user_id>/ | GET
users can view a request | /api/v1/requests/<user_id>/<reqest_id> | GET
users can modify their requests | /api/v1/requests/<user_id>/<reqest_id> | PUT
users can delete a request | /api/v1/requests/<user_id>/<reqest_id> | DELETE

*Testing*
> you could test each endpoint on postman or curl
> you could also run
`nosetests`
or
`pytest`

*this readme will be updated periodically*
### Author

*Lawrence Chege*

### Acknowledgement

*Andela Kenya*








