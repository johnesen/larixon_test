#!/bin/sh
until cd /opt/applications/larixon/src
do
    echo "Waiting for server volume..."
done

celery -A config worker -l info --beat