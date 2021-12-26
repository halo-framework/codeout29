# coding: utf-8

from __future__ import absolute_import
import unittest
import os
from flask import json
from six import BytesIO

from tester.app.dto.inline_response20011 import InlineResponse20011  # noqa: E501
from tester.app.dto.inline_response20014 import InlineResponse20014  # noqa: E501
from tester.app.dto.inline_response20017 import InlineResponse20017  # noqa: E501
from tester.app.dto.inline_response2002 import InlineResponse2002  # noqa: E501
from tester.app.dto.inline_response20021 import InlineResponse20021  # noqa: E501
from tester.app.dto.inline_response20024 import InlineResponse20024  # noqa: E501
from tester.app.dto.inline_response2005 import InlineResponse2005  # noqa: E501
from tester.app.dto.inline_response2006 import InlineResponse2006  # noqa: E501
from tester.app.dto.inline_response2008 import InlineResponse2008  # noqa: E501
from tester.test import BaseTestCase
from halo_app.const import LOC,DEV,TST,PRD

if 'HALO_STAGE' in os.environ:
    STAGE = os.environ['HALO_STAGE']
else:
    STAGE = LOC


class TestRetrieveController(BaseTestCase):
    """RetrieveController integration test stubs"""

    def test_retrieve_current_account(self):
        """Test case for retrieve_current_account

        Invoke a reporting action to obtain a Current Account Fulfillment Arrangement instance related report
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_behavior_qualifier_reference_ids(self):
        """Test case for retrieve_current_account_behavior_qualifier_reference_ids

        Retrieve Behavior Qualifier Reference Ids
        """
        path = "/" + STAGE
        query_string = [('collection-filter', 'collection_filter_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/{behavior_qualifier}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)behavior_qualifier='behavior_qualifier_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_behavior_qualifiers(self):
        """Test case for retrieve_current_account_behavior_qualifiers

        Retrieve BQ names
        """
        path = "/" + STAGE
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/current-account-fulfillment-arrangement/behavior-qualifiers/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_account_lien(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_account_lien

        Invoke a reporting action to obtain a AccountLien instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountlien/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_account_sweep(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_account_sweep

        Invoke a reporting action to obtain a AccountSweep instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/accountsweep/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals

        Invoke a reporting action to obtain a DepositsAndWithdrawals instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/depositsandwithdrawals/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_interest(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_interest

        Invoke a reporting action to obtain a Interest instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/interest/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_issued_device(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_issued_device

        Invoke a reporting action to obtain a IssuedDevice instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/issueddevice/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_payments(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_payments

        Invoke a reporting action to obtain a Payments instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/payments/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_fulfillment_arrangement_service_fees(self):
        """Test case for retrieve_current_account_fulfillment_arrangement_service_fees

        Invoke a reporting action to obtain a ServiceFees instance related report.
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement/{cr_reference_id}/servicefees/{bq_reference_id}'.format(sd_reference_id='sd_reference_id_example',)cr_reference_id='cr_reference_id_example',)bq_reference_id='bq_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_current_account_reference_ids(self):
        """Test case for retrieve_current_account_reference_ids

        Retrieve CR Ids
        """
        path = "/" + STAGE
        query_string = [('collection-filter', 'collection_filter_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}/current-account-fulfillment-arrangement'.format(sd_reference_id='sd_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_sd_current_account(self):
        """Test case for retrieve_sd_current_account

        Analytical views maintained by the SDCurrentAccount service center for management reporting and analysis purposes
        """
        path = "/" + STAGE
        query_string = [('queryparams', 'queryparams_example')]
        headers = { 
            'Ocp-Apim-Subscription-Key': self.app.config['API_KEY'],
            'Accept': 'application/json',
            'apiKeyHeader': 'special-key',
        }
        response = self.client.open(path+
            '/current-account/{sd_reference_id}'.format(sd_reference_id='sd_reference_id_example',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
