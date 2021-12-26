# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object2 import InlineObject2  # noqa: E501
from tester.app.dto.inline_response2001 import InlineResponse2001  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestFeedbackController(BaseTestCase):
    """FeedbackController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_feedback_sd_current_account(self):
        """Test case for feedback_sd_current_account

        Capturing feedback against the SDCurrentAccount service that can target different levels of detail: SD/CR/BQ
        """
        path = "/" + STAGE
        body = tester.InlineObject2()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/feedback'.format(sd_reference_id='sd_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
