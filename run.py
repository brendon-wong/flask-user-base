"""Run the app in development."""

from project.app import create_app

# Do not run the app if it is being imported
if __name__ == '__main__':
    app = create_app()
    app.run()
