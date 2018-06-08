# Flask-User-Base

Flask-User-Base is a Flask boilerplate app that makes it easy to create a web application that can support users. The app only uses Flask and common Flask extensions to minimize the learning curve. The extension Flask-User handles all user related code including user registration, user login, email confirmation, and password resets so the developer can get started with writing application specific code. A secondary purpose of this repository is to demonstrate how to incorporate Flask-User in a Flask project.

Flask-User has been implemented in the models to support all optional data-models including multiple email accounts per user and user roles. These can be easily changed if needed by referring to the Flask-User [data-models documentation](http://flask-user.readthedocs.io/en/latest/data_models.html). Flask-User's built in templates have been duplicated in a directory in the application's primary templates folder to allow for Flask-User's templates to be customized if desired, as documented [here](http://flask-user.readthedocs.io/en/latest/unused.html#customizingformtemplates). If no customization is desired, all Flask-User templates can be removed from the templates folder.

This app can be deployed on Heroku immediately and includes the Heroku-related files `Procfile` and `runtime.txt`. These files can be removed if Heroku deployment is not needed.

Inside the config.py files and the setup.py file, the app is referred to as "Project." A case sensitive search and "replace all" operation in the project's root directory is all that is needed to customize the name of the app.

The following instructions are for MacOS. See the [Installation](http://flask.pocoo.org/docs/latest/installation/) part of the Flask documentation to run the app on other operating systems.

## To set up the application:
1. `git clone` this repository
2. `python3 -m venv venv` to create a new virtual environment
3. `. venv/bin/activate` to activate the virtual environment (deactivate the virtual environment with `deactivate`)
4. `pip3 install -r requirements.txt` to install/update all requirements
5. `pip3 install --editable .` in the root directory to install the application package

## To run the application:
1. `. venv/bin/activate` to activate the virtual environment
2. `python3 run.py` to run the app
3. View the app in a web browser at http://localhost:5000

## Local database setup
0. The application is configured to create a sqlite database called dev.db in the top-level folder when it is run locally
1. `flask db init` to create the migration repository
2. `flask db migrate` to have Alembic compare the db schema with db file
3. `flask db upgrade` to apply changes to the db file

## Heroku Deployment
1. On Heroku, set the environment variable ENV to 'prod' which loads config.py from the instance folder instead of the root directory
2. `heroku addons:add heroku-postgresql:hobby-dev` to create a Postgres database 
3. Set SQLALCHEMY_DATABASE_URI to Heroku's DATABASE_URL environment variable in the config.py file in Flask's instance folder
4. Use Flask Migrate's `flask db init` and `flask db migrate` commands to generate migrations
5. Push the migrations folder to Heroku
6. `heroku run python3 manage.py db upgrade --app app-name` to upgrade the production database

## Running Postgres locally
0.  `brew install postgresql` to install Postgres with Homebrew
1. `brew services start postgresql` to start
2. `brew services stop postgresql` to stop

## Locally Create Heroku Migrations
Source: https://stackoverflow.com/questions/21529118/running-flask-migrate-on-heroku-produces-error
1. Use the command `heroku pg:pull DATABASE_URL new_db_name -a heroku_app_name` which creates a new local Postgres database with the name new_db_name and the same database schema and content of your Postgres database on Heroku. A database with the same name must not already exist. You can use a tool like Postico to view and manage your local Postgres databases with a GUI.
2. Configure your Flask app to use the new Postgres database. Assuming Flask-SQLAlchemy is being used, in Flask's configuration set `SQLALCHEMY_DATABASE_URI = "postgresql://localhost/new_db_name"`.
3. Now that Flask recognizes the new local Postgres database mirroring the production database, use Flask-Migrate's `flask db init` and `flask db migrate` commands to generate a migration script.
4. Push the migrations folder generated by Flask-Migrate to Heroku.
5. Use Flask-Migrate to upgrade the production database on Heroku with `heroku run flask db upgrade -a heroku_app_name`.

## Brendon's development notes
- Create readme.md with https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- Create requirements.txt with https://devcenter.heroku.com/articles/python-pip
- Create app structure as a package with http://exploreflask.com/en/latest/organizing.html and https://damyanon.net/post/flask-series-structure/
- Create setup.py with http://flask.pocoo.org/docs/1.0/patterns/distribute/
- Heroku deployment with https://github.com/datademofun/heroku-basic-flask and many other sources, see https://medium.com/@AndreyAzimov/how-free-heroku-really-works-and-how-to-get-maximum-from-it-daa53f2b3c57 for maximizing the free tier
- Add Flask-User with Flask User's example apps http://flask-user.readthedocs.io/en/latest/quickstart.html
- Postgres configuration with https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/ and https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku
- Add Flask-Admin with https://flask-admin.readthedocs.io/en/latest/, protect index page with https://stackoverflow.com/questions/31091637/how-to-secure-the-flask-admin-panel-with-flask-security?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
- Manage remote migrations with https://stackoverflow.com/questions/21529118/running-flask-migrate-on-heroku-produces-error?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
- Configure Postgres locally with https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

## Inspiration
- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)
- [cookiecutter-flask-minimal](https://github.com/candidtim/cookiecutter-flask-minimal)
- [Explore Flask](http://exploreflask.com/en/latest/)
