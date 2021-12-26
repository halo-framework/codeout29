# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object10 import InlineObject10  # noqa: E501
from tester.app.dto.inline_object19 import InlineObject19  # noqa: E501
from tester.app.dto.inline_response20010 import InlineResponse20010  # noqa: E501
from tester.app.dto.inline_response20019 import InlineResponse20019  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestExchangeController(BaseTestCase):
    """ExchangeController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_exchange_current_account_fulfillment_arrangement_account_lien_update(self):
        """Test case for exchange_current_account_fulfillment_arrangement_account_lien_update

        Handle an external exchange (e.g. accept, reject, verify)
        """
        path = "/" + STAGE
        body = tester.InlineObject10()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountlien/{bq_reference_id}/exchange'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_exchange_current_account_fulfillment_arrangement_payments_update(self):
        """Test case for exchange_current_account_fulfillment_arrangement_payments_update

        Handle an external exchange (e.g. accept, reject, verify)
        """
        path = "/" + STAGE
        body = tester.InlineObject19()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/payments/{bq_reference_id}/exchange'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
