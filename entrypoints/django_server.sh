#!/bin/sh
cd src
echo "Starting makemigrations command"
python manage.py makemigrations
echo "Starting migrate command"
python manage.py migrate
echo "Starting collectstatic command"
python manage.py collectstatic --no-input
echo "Starting server"
gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 6 --threads 4