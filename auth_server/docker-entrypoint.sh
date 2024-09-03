#!/bin/sh
python manage.py migrate
gunicorn auth_server.wsgi:application --bind 0.0.0.0:8000