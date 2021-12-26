# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object23 import InlineObject23  # noqa: E501
from tester.app.dto.inline_response20023 import InlineResponse20023  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestRequestController(BaseTestCase):
    """RequestController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_request_current_account_fulfillment_arrangement_issued_device_update(self):
        """Test case for request_current_account_fulfillment_arrangement_issued_device_update

        Invoke a service request action against the IssuedDevice instance
        """
        path = "/" + STAGE
        body = tester.InlineObject23()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/issueddevice/{bq_reference_id}/requisition'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
