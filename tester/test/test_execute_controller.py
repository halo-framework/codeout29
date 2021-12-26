# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object13 import InlineObject13  # noqa: E501
from tester.app.dto.inline_object16 import InlineObject16  # noqa: E501
from tester.app.dto.inline_object20 import InlineObject20  # noqa: E501
from tester.app.dto.inline_object7 import InlineObject7  # noqa: E501
from tester.app.dto.inline_response20013 import InlineResponse20013  # noqa: E501
from tester.app.dto.inline_response20016 import InlineResponse20016  # noqa: E501
from tester.app.dto.inline_response20020 import InlineResponse20020  # noqa: E501
from tester.app.dto.inline_response2007 import InlineResponse2007  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestExecuteController(BaseTestCase):
    """ExecuteController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_execute_current_account_fulfillment_arrangement_account_sweep_update(self):
        """Test case for execute_current_account_fulfillment_arrangement_account_sweep_update

        Invoke an automated execute action against the AccountSweep instance
        """
        path = "/" + STAGE
        body = tester.InlineObject13()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountsweep/{bq_reference_id}/execution'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_execute_current_account_fulfillment_arrangement_deposits_and_withdrawals_update(self):
        """Test case for execute_current_account_fulfillment_arrangement_deposits_and_withdrawals_update

        Invoke an automated execute action against the DepositsAndWithdrawals instance
        """
        path = "/" + STAGE
        body = tester.InlineObject16()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/depositsandwithdrawals/{bq_reference_id}/execution'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_execute_current_account_fulfillment_arrangement_payments_update(self):
        """Test case for execute_current_account_fulfillment_arrangement_payments_update

        Invoke an automated execute action against the Payments instance
        """
        path = "/" + STAGE
        body = tester.InlineObject20()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/payments/{bq_reference_id}/execution'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_execute_current_account_fulfillment_arrangement_service_fees_update(self):
        """Test case for execute_current_account_fulfillment_arrangement_service_fees_update

        Invoke an automated execute action against the ServiceFees instance
        """
        path = "/" + STAGE
        body = tester.InlineObject7()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/servicefees/{bq_reference_id}/execution'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
