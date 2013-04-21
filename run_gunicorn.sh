#!/bin/sh
gunicorn --bind=127.0.0.1:9000 pomysl.wsgi:application -c gunicorn.py.ini
