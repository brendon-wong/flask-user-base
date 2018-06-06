"""
Test public blueprint.

Testing in Flask: http://flask.pocoo.org/docs/1.0/testing/

"""
from werkzeug.wrappers import Response

def test_home(app):
    # Response object: http://flask.pocoo.org/docs/0.12/api/#response-objects
    res = app.get("/")
    assert res.status_code == 200
    assert b"Project" in res.data