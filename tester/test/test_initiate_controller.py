# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_object11 import InlineObject11  # noqa: E501
from tester.app.dto.inline_object14 import InlineObject14  # noqa: E501
from tester.app.dto.inline_object17 import InlineObject17  # noqa: E501
from tester.app.dto.inline_object21 import InlineObject21  # noqa: E501
from tester.app.dto.inline_object3 import InlineObject3  # noqa: E501
from tester.app.dto.inline_object6 import InlineObject6  # noqa: E501
from tester.app.dto.inline_object8 import InlineObject8  # noqa: E501
from tester.app.dto.inline_response2011 import InlineResponse2011  # noqa: E501
from tester.app.dto.inline_response2012 import InlineResponse2012  # noqa: E501
from tester.app.dto.inline_response2013 import InlineResponse2013  # noqa: E501
from tester.app.dto.inline_response2014 import InlineResponse2014  # noqa: E501
from tester.app.dto.inline_response2015 import InlineResponse2015  # noqa: E501
from tester.app.dto.inline_response2016 import InlineResponse2016  # noqa: E501
from tester.app.dto.inline_response2017 import InlineResponse2017  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestInitiateController(BaseTestCase):
    """InitiateController integration test stubs"""

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement(self):
        """Test case for initiate_current_account_fulfillment_arrangement

        Details of a new CurrentAccountFulfillmentArrangement instance
        """
        path = "/" + STAGE
        body = tester.InlineObject3()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/initiation'.format(sd_reference_id='sd_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_account_lien(self):
        """Test case for initiate_current_account_fulfillment_arrangement_account_lien

        Details of a new AccountLien instance
        """
        path = "/" + STAGE
        body = tester.InlineObject8()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountlien/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_account_sweep(self):
        """Test case for initiate_current_account_fulfillment_arrangement_account_sweep

        Details of a new AccountSweep instance
        """
        path = "/" + STAGE
        body = tester.InlineObject11()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountsweep/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_deposits_and_withdrawals(self):
        """Test case for initiate_current_account_fulfillment_arrangement_deposits_and_withdrawals

        Details of a new DepositsAndWithdrawals instance
        """
        path = "/" + STAGE
        body = tester.InlineObject14()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/depositsandwithdrawals/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_issued_device(self):
        """Test case for initiate_current_account_fulfillment_arrangement_issued_device

        Details of a new IssuedDevice instance
        """
        path = "/" + STAGE
        body = tester.InlineObject21()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/issueddevice/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_payments(self):
        """Test case for initiate_current_account_fulfillment_arrangement_payments

        Details of a new Payments instance
        """
        path = "/" + STAGE
        body = tester.InlineObject17()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/payments/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
    def test_initiate_current_account_fulfillment_arrangement_service_fees(self):
        """Test case for initiate_current_account_fulfillment_arrangement_service_fees

        Details of a new ServiceFees instance
        """
        path = "/" + STAGE
        body = tester.InlineObject6()
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/servicefees/initiation'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
