""" Pytest fixtures, documented here: http://pytest.readthedocs.io/en/latest/fixture.html

You can auto-discover and run all tests with: $ pytest

Use: $ pytest --cov=project tests/ to examine test coverage
     $ pytest --cov=project works the same as of 5/3/2018
     
Flake8: $ flake8 path/to/code/

Documentation:

* https://docs.pytest.org/en/latest/
* https://docs.pytest.org/en/latest/fixture.html
* http://flask.pocoo.org/docs/latest/testing/
"""

import pytest

from project.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app.test_client()