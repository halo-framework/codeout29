# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object1 import InlineObject1  # noqa: E501
from tester.app.dto.inline_response200 import InlineResponse200  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestConfigureController(BaseTestCase):
    """ConfigureController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_configure_sd_current_account(self):
        """Test case for configure_sd_current_account

        Update an active SDCurrentAccount session configuration
        """
        path = "/" + STAGE
        body = tester.InlineObject1()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/configuration'.format(sd_reference_id='sd_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
