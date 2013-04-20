#!/bin/sh
gunicorn --workers=4 --bind=127.0.0.1:9000 pomysl.wsgi:application
