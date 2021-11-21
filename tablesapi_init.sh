#!/bin/bash

#echo "PREPARE DATABASE..."
echo "Change directory to roo of project..."
cd ..

echo "Collect static files..."
python manage.py collectstatic --noinput

# echo "Получение дампа данных только при первом запуске контейнера"
# python manage.py loaddata datadump.json

# echo "Apply database migrations... только при первом запуске контейнера"
# python manage.py migrate

echo "Starting server..."
#echo "Django development server..."
#python manage.py runserver 0.0.0.0:8082

echo "Gunicorn server"
gunicorn -b 0.0.0.0:8082 config.wsgi:application

