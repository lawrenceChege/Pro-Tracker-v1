web: gunicorn run:app
gunicorn project.wsgi:application --preload --workers 1
release: python migrations.py db upgrade