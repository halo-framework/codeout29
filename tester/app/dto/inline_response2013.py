# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2013_account_lien_instance_record import InlineResponse2013AccountLienInstanceRecord
from tester.app.dto.inline_response2013_current_account_fulfillment_arrangement_instance_record import InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord
from tester import util

from tester.app.dto.inline_response2013_account_lien_instance_record import InlineResponse2013AccountLienInstanceRecord  # noqa: E501
from tester.app.dto.inline_response2013_current_account_fulfillment_arrangement_instance_record import InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501



class InlineResponse2013(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, account_lien_instance_reference=None, account_lien_initiate_action_reference=None, account_lien_initiate_action_record=None, account_lien_instance_status=None, account_lien_instance_record=None):  # noqa: E501
        """InlineResponse2013 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2013.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord
        :param account_lien_instance_reference: The account_lien_instance_reference of this InlineResponse2013.  # noqa: E501
        :type account_lien_instance_reference: str
        :param account_lien_initiate_action_reference: The account_lien_initiate_action_reference of this InlineResponse2013.  # noqa: E501
        :type account_lien_initiate_action_reference: str
        :param account_lien_initiate_action_record: The account_lien_initiate_action_record of this InlineResponse2013.  # noqa: E501
        :type account_lien_initiate_action_record: object
        :param account_lien_instance_status: The account_lien_instance_status of this InlineResponse2013.  # noqa: E501
        :type account_lien_instance_status: str
        :param account_lien_instance_record: The account_lien_instance_record of this InlineResponse2013.  # noqa: E501
        :type account_lien_instance_record: InlineResponse2013AccountLienInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord,
            'account_lien_instance_reference': str,
            'account_lien_initiate_action_reference': str,
            'account_lien_initiate_action_record': object,
            'account_lien_instance_status': str,
            'account_lien_instance_record': InlineResponse2013AccountLienInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'account_lien_instance_reference': 'accountLienInstanceReference',
            'account_lien_initiate_action_reference': 'accountLienInitiateActionReference',
            'account_lien_initiate_action_record': 'accountLienInitiateActionRecord',
            'account_lien_instance_status': 'accountLienInstanceStatus',
            'account_lien_instance_record': 'accountLienInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._account_lien_instance_reference = account_lien_instance_reference
        self._account_lien_initiate_action_reference = account_lien_initiate_action_reference
        self._account_lien_initiate_action_record = account_lien_initiate_action_record
        self._account_lien_instance_status = account_lien_instance_status
        self._account_lien_instance_record = account_lien_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2013':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_3 of this InlineResponse2013.  # noqa: E501
        :rtype: InlineResponse2013
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2013.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2013.
        :rtype: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2013.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2013.
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def account_lien_instance_reference(self):
        """Gets the account_lien_instance_reference of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :return: The account_lien_instance_reference of this InlineResponse2013.
        :rtype: str
        """
        return self._account_lien_instance_reference

    @account_lien_instance_reference.setter
    def account_lien_instance_reference(self, account_lien_instance_reference):
        """Sets the account_lien_instance_reference of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :param account_lien_instance_reference: The account_lien_instance_reference of this InlineResponse2013.
        :type account_lien_instance_reference: str
        """

        self._account_lien_instance_reference = account_lien_instance_reference

    @property
    def account_lien_initiate_action_reference(self):
        """Gets the account_lien_initiate_action_reference of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :return: The account_lien_initiate_action_reference of this InlineResponse2013.
        :rtype: str
        """
        return self._account_lien_initiate_action_reference

    @account_lien_initiate_action_reference.setter
    def account_lien_initiate_action_reference(self, account_lien_initiate_action_reference):
        """Sets the account_lien_initiate_action_reference of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :param account_lien_initiate_action_reference: The account_lien_initiate_action_reference of this InlineResponse2013.
        :type account_lien_initiate_action_reference: str
        """

        self._account_lien_initiate_action_reference = account_lien_initiate_action_reference

    @property
    def account_lien_initiate_action_record(self):
        """Gets the account_lien_initiate_action_record of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The account_lien_initiate_action_record of this InlineResponse2013.
        :rtype: object
        """
        return self._account_lien_initiate_action_record

    @account_lien_initiate_action_record.setter
    def account_lien_initiate_action_record(self, account_lien_initiate_action_record):
        """Sets the account_lien_initiate_action_record of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param account_lien_initiate_action_record: The account_lien_initiate_action_record of this InlineResponse2013.
        :type account_lien_initiate_action_record: object
        """

        self._account_lien_initiate_action_record = account_lien_initiate_action_record

    @property
    def account_lien_instance_status(self):
        """Gets the account_lien_instance_status of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Account Lien instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The account_lien_instance_status of this InlineResponse2013.
        :rtype: str
        """
        return self._account_lien_instance_status

    @account_lien_instance_status.setter
    def account_lien_instance_status(self, account_lien_instance_status):
        """Sets the account_lien_instance_status of this InlineResponse2013.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Account Lien instance (e.g. initialised, pending, active)   # noqa: E501

        :param account_lien_instance_status: The account_lien_instance_status of this InlineResponse2013.
        :type account_lien_instance_status: str
        """

        self._account_lien_instance_status = account_lien_instance_status

    @property
    def account_lien_instance_record(self):
        """Gets the account_lien_instance_record of this InlineResponse2013.


        :return: The account_lien_instance_record of this InlineResponse2013.
        :rtype: InlineResponse2013AccountLienInstanceRecord
        """
        return self._account_lien_instance_record

    @account_lien_instance_record.setter
    def account_lien_instance_record(self, account_lien_instance_record):
        """Sets the account_lien_instance_record of this InlineResponse2013.


        :param account_lien_instance_record: The account_lien_instance_record of this InlineResponse2013.
        :type account_lien_instance_record: InlineResponse2013AccountLienInstanceRecord
        """

        self._account_lien_instance_record = account_lien_instance_record