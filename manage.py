"""Run a command to use Alembic to upgrade the database with 
"heroku run python manage.py db upgrade --app app-name" on the Heroku CLI.

This file is currently unused because "heroku run flask db upgrade -a app-name" 
also works for database operations.
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project.app import create_app, db

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
