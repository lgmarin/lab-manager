#!/bin/bash

source venv/bin/activate
sleep 10
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app