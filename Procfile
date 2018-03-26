web: gunicorn app:app --preload
web: gunicorn app:app --log-file -

release: python manage.py db upgrade
