"""Run the app in production with gunicorn."""

from project.app import create_app

# Provides an application object to be used by the server
app = create_app()
