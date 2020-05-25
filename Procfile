release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn gallery.wsgi --log-file -