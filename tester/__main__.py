#!/usr/bin/env python3

import os
import connexion
from flask import Flask
from tester import encoder
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC

def create_app()-> Flask:
    _app = connexion.App(__name__, specification_dir='entrypoints/rest/openapi/')
    _app.app.json_encoder = encoder.JSONEncoder
    with _app.app.app_context():
        path = "/" + STAGE
        _app.add_api('openapi.yaml',base_path=path,
                     arguments={'title': 'current-accountv2'},
                     pythonic_params=True)
        configure_app(_app.app)
        setup_app(_app.app)
        register_halo(_app.app)
        register_shellcontext(_app.app)
        register_commands(_app.app)

        URL = 'http://{host}:{port}{url_prefix}/ui/'.format(
            host=_app.app.config['HOST'],
            port=_app.app.config['PORT'],
            url_prefix=path)
        print('[✔] API documentation (Swagger UI) available at: {}'.format(URL))

        return _app


def configure_app(flask_app:Flask):
    flask_app.config.from_object(f"tester.entrypoints.config.Config_{os.getenv('HALO_STAGE', LOC)}")

def setup_app(flask_app:Flask):
    from tester.app.hooks import before_first_request_func,before_request_func,after_request_func,teardown_request_func

    @flask_app.before_first_request
    def before_first_request():
        # do something
        before_first_request_func()

    @flask_app.before_request
    def before_request():
        # do something
        before_request_func()

    @flask_app.after_request
    def after_request(response):
        # get the request object somehow
        return after_request_func(response)

    @flask_app.teardown_request
    def teardown_request(error=None):
        # get the request object somehow
        teardown_request_func(error)

def register_halo(flask_app: Flask):
    with flask_app.app_context():
        from halo_app.ssm import set_app_param_config, set_host_param_config
        from halo_app.infra.apis import load_api_config
        from halo_app.app.globals import load_global_data
        from halo_app.base_util import BaseUtil
        #flask_app.config["SSM_TYPE"] = 'ONPREM'
        flask_app.config["APP_NAME"] = "abc"
        flask_app.config["FUNC_NAME"] = "def"
        if 'SSM_TYPE' in flask_app.config and flask_app.config['SSM_TYPE'] != 'NONE':
            load_api_config(flask_app.config['ENV_TYPE'], flask_app.config['SSM_TYPE'], flask_app.config['FUNC_NAME'],
                            flask_app.config['API_CONFIG'])
            HALO_HOST = BaseUtil.get_host_name()
            params = {}
            params["url"] = set_host_param_config(HALO_HOST)
            set_app_param_config(flask_app.config['SSM_TYPE'], params )
        if 'INIT_DATA_MAP' in flask_app.config and 'INIT_CLASS_NAME' in flask_app.config:
            data_map = flask_app.config['INIT_DATA_MAP']
            class_name = flask_app.config['INIT_CLASS_NAME']
            load_global_data(class_name, data_map)
        else:
            file_dir = os.path.dirname(__file__)
            PROP_URL = os.path.join(file_dir, '..', 'env', 'config', "startup_props.json")
            flask_app.config["INIT_CLASS_NAME"] = 'halo_bian.bian.app.handler.BianGlobalService'
            flask_app.config["INIT_DATA_MAP"] = {'INIT_STATE': "Idle", 'PROP_URL': PROP_URL}
            load_global_data(flask_app.config["INIT_CLASS_NAME"], flask_app.config["INIT_DATA_MAP"])


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': api.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""


if __name__ == '__main__':
    app = create_app()
    app.run(port=app.app.config["PORT"])