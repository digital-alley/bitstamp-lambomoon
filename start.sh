#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn wsgi:application \
  		--bind 0.0.0.0:8000
