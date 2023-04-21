#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

# exec gunicorn server.wsgi:application \
#     --bind 0.0.0.0:8000 \
#     --workers 3 \
#     --reload

exec python manage.py runserver 0.0.0.0:8000

# exec python manage.py process_static_files &
# watchdog_pid=$!

# wait $watchdog_pid