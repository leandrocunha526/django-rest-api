# Django REST API
## To run
### Create a virtualenv environment
Install in Debian based distributions 

`apt install python3-pip virtualenv python3-dev default-libmysqlclient-dev build-essential`

Create virtualenv

`virtualenv -p python3 venv`

Set virtualenv environment

`. venv/bin/activate`

### Install dependencies with pip
`pip install -r requirements.txt`

### Migrate database

The project need MariaDB or MySQL to database and settings in `/api/settings`.

Create folder `products/migrations` and archive `__init__.py`.

Make migrations

`python3 manage.py makemigrations`

Run migrate

`python manage.py migrate`

Run server

`python manage.py runserver`

API root: http://localhost:8000

Admin: http://localhost:8000/admin

## Requirements

- Django 4.0
- Django Rest Framework 3.13
- Python versions 3.8 or 3.9 (is not work with 3.10, please wait)

See [requirements.txt](requirements.txt)

## Docs

- [Quick start Django Rest Framework](https://www.django-rest-framework.org/tutorial/quickstart/)
