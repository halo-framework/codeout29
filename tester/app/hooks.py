    #!/usr/bin/env python3

import logging
import urllib
import uuid
import requests
import datetime
import json
import traceback
from flask import g,request,session



from halo_app.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)


def before_first_request_func():

    """
    This function will run once before the first request to this instance of the application.
    You may want to use this function to create any databases/tables required for your app.
    """

    print("This function will run once ")


def before_request_func():

    """
    This function will run before every request. Let's add something to the session & g.
    It's a good place for things like establishing database connections, retrieving
    user information from the session, assigning values to the flask g object etc..
    We have access to the request context.
    """

    request_id = request.headers.get('X-Request-ID')

    if not request_id:
        request_id = uuid.uuid4().__str__()

    g.request_id = request_id
    print("before_request is running!")



def after_request_func(response):

    """
    This function will run after a request, as long as no exceptions occur.
    It must take and return the same parameter - an instance of response_class.
    This is a good place to do some application cleanup.
    """

    response.headers.add('X-Request-ID', g.request_id)
    print("after_request is running!", g.request_id)
    return response


def teardown_request_func(error=None):

    """
    This function will run after a request, regardless if an exception occurs or not.
    It's a good place to do some cleanup, such as closing any database connections.
    If an exception is raised, it will be passed to the function.
    You should so everything in your power to ensure this function does not fail, so
    liberal use of try/except blocks is recommended.
    """

    print("teardown_request is running!")
    if error:
        # Log the error
        print(str(error))

