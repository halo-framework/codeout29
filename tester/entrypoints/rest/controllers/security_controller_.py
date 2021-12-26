from typing import List


def info_from_apiKeyHeader(api_key, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """
    from flask import current_app as flask_app
    API_KEYS = "API_KEYS"
    if API_KEYS in flask_app.config and api_key in flask_app.config[API_KEYS]:
        return {'uid': 'user_id'}
    return None



