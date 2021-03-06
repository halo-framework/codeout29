import logging
import os
import connexion
#from unittest import TestCase
from flask_testing import TestCase
from halo_app.const import LOC,DEV,TST,PRD
from tester.__main__ import create_app as orig_create_app
from tester.encoder import JSONEncoder

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC

class BaseTestCase(TestCase):

    def create_app_base(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../entrypoints/rest/openapi/')
        app.app.json_encoder = JSONEncoder
        path = "/" + STAGE
        app.add_api('openapi.yaml', base_path=path,arguments={'title': 'current-accountv2'},
            pythonic_params=True)
        return app.app

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        return orig_create_app().app
