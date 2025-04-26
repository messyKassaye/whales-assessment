#!/bin/bash

# Exit on error
set -e

# Run database migrations
echo "Running makemigrations and migrate..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Start Gunicorn server
echo "Starting Gunicorn server..."
gunicorn todoapi.wsgi:application --bind 0.0.0.0:8000
