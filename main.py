from urlshortener.wsgi import application
# This file imports the WSGI-compatible object of your Django app,
# application from urlshortener/wsgi.py and renames it app so it is discoverable by
# App Engine without additional configuration.
app = application