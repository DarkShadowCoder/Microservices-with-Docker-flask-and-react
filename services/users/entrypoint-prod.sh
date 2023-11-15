#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"
gunicorn -b 127.0.0.1:5000 manage:app
