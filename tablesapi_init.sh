#!/bin/bash

#echo "PREPARE DATABASE..."

# cd ./app/acts

#echo "Collect static files..."
#python manage.py collectstatic --noinput

# echo "Получение дампа данных только при первом запуске контейнера"
# python manage.py loaddata datadump.json

# echo "Apply database migrations... только при первом запуске контейнера"
# python manage.py migrate

echo "Starting server..."
#echo "Django development server..."
#python manage.py runserver 0.0.0.0:8082

echo "Gunicorn server"
cd ..
gunicorn -b 0.0.0.0:8082 config.wsgi:application

