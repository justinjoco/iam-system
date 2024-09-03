#!/bin/sh
echo "Starting api_server..."
python manage.py migrate
gunicorn api_server.wsgi:application --bind 0.0.0.0:8000