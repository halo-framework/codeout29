# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object12 import InlineObject12  # noqa: E501
from tester.app.dto.inline_object15 import InlineObject15  # noqa: E501
from tester.app.dto.inline_object18 import InlineObject18  # noqa: E501
from tester.app.dto.inline_object22 import InlineObject22  # noqa: E501
from tester.app.dto.inline_object4 import InlineObject4  # noqa: E501
from tester.app.dto.inline_object9 import InlineObject9  # noqa: E501
from tester.app.dto.inline_response20012 import InlineResponse20012  # noqa: E501
from tester.app.dto.inline_response20015 import InlineResponse20015  # noqa: E501
from tester.app.dto.inline_response20018 import InlineResponse20018  # noqa: E501
from tester.app.dto.inline_response20022 import InlineResponse20022  # noqa: E501
from tester.app.dto.inline_response2003 import InlineResponse2003  # noqa: E501
from tester.app.dto.inline_response2009 import InlineResponse2009  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestUpdateController(BaseTestCase):
    """UpdateController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement(self):
        """Test case for update_current_account_fulfillment_arrangement

        Update to any amendable fields of the CurrentAccountFulfillmentArrangement instance
        """
        path = "/" + STAGE
        body = tester.InlineObject4()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement_account_lien(self):
        """Test case for update_current_account_fulfillment_arrangement_account_lien

        Update to any amendable fields of the AccountLien instance
        """
        path = "/" + STAGE
        body = tester.InlineObject9()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountlien/{bq_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement_account_sweep(self):
        """Test case for update_current_account_fulfillment_arrangement_account_sweep

        Update to any amendable fields of the AccountSweep instance
        """
        path = "/" + STAGE
        body = tester.InlineObject12()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountsweep/{bq_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement_deposits_and_withdrawals(self):
        """Test case for update_current_account_fulfillment_arrangement_deposits_and_withdrawals

        Update to any amendable fields of the DepositsAndWithdrawals instance
        """
        path = "/" + STAGE
        body = tester.InlineObject15()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/depositsandwithdrawals/{bq_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement_issued_device(self):
        """Test case for update_current_account_fulfillment_arrangement_issued_device

        Update to any amendable fields of the IssuedDevice instance
        """
        path = "/" + STAGE
        body = tester.InlineObject22()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/issueddevice/{bq_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_update_current_account_fulfillment_arrangement_payments(self):
        """Test case for update_current_account_fulfillment_arrangement_payments

        Update to any amendable fields of the Payments instance
        """
        path = "/" + STAGE
        body = tester.InlineObject18()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/payments/{bq_reference_id}/update'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
