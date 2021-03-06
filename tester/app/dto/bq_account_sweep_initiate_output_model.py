# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2012_current_account_fulfillment_arrangement_instance_record import InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
from tester.app.dto.inline_response2014_account_sweep_instance_record import InlineResponse2014AccountSweepInstanceRecord
from tester import util

from tester.app.dto.inline_response2012_current_account_fulfillment_arrangement_instance_record import InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501
from tester.app.dto.inline_response2014_account_sweep_instance_record import InlineResponse2014AccountSweepInstanceRecord  # noqa: E501



class BQAccountSweepInitiateOutputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, account_sweep_instance_reference=None, account_sweep_initiate_action_reference=None, account_sweep_initiate_action_record=None, account_sweep_instance_status=None, account_sweep_instance_record=None):  # noqa: E501
        """BQAccountSweepInitiateOutputModel - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        :param account_sweep_instance_reference: The account_sweep_instance_reference of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type account_sweep_instance_reference: str
        :param account_sweep_initiate_action_reference: The account_sweep_initiate_action_reference of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type account_sweep_initiate_action_reference: str
        :param account_sweep_initiate_action_record: The account_sweep_initiate_action_record of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type account_sweep_initiate_action_record: object
        :param account_sweep_instance_status: The account_sweep_instance_status of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type account_sweep_instance_status: str
        :param account_sweep_instance_record: The account_sweep_instance_record of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :type account_sweep_instance_record: InlineResponse2014AccountSweepInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord,
            'account_sweep_instance_reference': str,
            'account_sweep_initiate_action_reference': str,
            'account_sweep_initiate_action_record': object,
            'account_sweep_instance_status': str,
            'account_sweep_instance_record': InlineResponse2014AccountSweepInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'account_sweep_instance_reference': 'accountSweepInstanceReference',
            'account_sweep_initiate_action_reference': 'accountSweepInitiateActionReference',
            'account_sweep_initiate_action_record': 'accountSweepInitiateActionRecord',
            'account_sweep_instance_status': 'accountSweepInstanceStatus',
            'account_sweep_instance_record': 'accountSweepInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._account_sweep_instance_reference = account_sweep_instance_reference
        self._account_sweep_initiate_action_reference = account_sweep_initiate_action_reference
        self._account_sweep_initiate_action_record = account_sweep_initiate_action_record
        self._account_sweep_instance_status = account_sweep_instance_status
        self._account_sweep_instance_record = account_sweep_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountSweepInitiateOutputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountSweepInitiateOutputModel of this BQAccountSweepInitiateOutputModel.  # noqa: E501
        :rtype: BQAccountSweepInitiateOutputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this BQAccountSweepInitiateOutputModel.


        :return: The current_account_fulfillment_arrangement_instance_record of this BQAccountSweepInitiateOutputModel.
        :rtype: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this BQAccountSweepInitiateOutputModel.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this BQAccountSweepInitiateOutputModel.
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def account_sweep_instance_reference(self):
        """Gets the account_sweep_instance_reference of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Sweep instance   # noqa: E501

        :return: The account_sweep_instance_reference of this BQAccountSweepInitiateOutputModel.
        :rtype: str
        """
        return self._account_sweep_instance_reference

    @account_sweep_instance_reference.setter
    def account_sweep_instance_reference(self, account_sweep_instance_reference):
        """Sets the account_sweep_instance_reference of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Sweep instance   # noqa: E501

        :param account_sweep_instance_reference: The account_sweep_instance_reference of this BQAccountSweepInitiateOutputModel.
        :type account_sweep_instance_reference: str
        """

        self._account_sweep_instance_reference = account_sweep_instance_reference

    @property
    def account_sweep_initiate_action_reference(self):
        """Gets the account_sweep_initiate_action_reference of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :return: The account_sweep_initiate_action_reference of this BQAccountSweepInitiateOutputModel.
        :rtype: str
        """
        return self._account_sweep_initiate_action_reference

    @account_sweep_initiate_action_reference.setter
    def account_sweep_initiate_action_reference(self, account_sweep_initiate_action_reference):
        """Sets the account_sweep_initiate_action_reference of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :param account_sweep_initiate_action_reference: The account_sweep_initiate_action_reference of this BQAccountSweepInitiateOutputModel.
        :type account_sweep_initiate_action_reference: str
        """

        self._account_sweep_initiate_action_reference = account_sweep_initiate_action_reference

    @property
    def account_sweep_initiate_action_record(self):
        """Gets the account_sweep_initiate_action_record of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The account_sweep_initiate_action_record of this BQAccountSweepInitiateOutputModel.
        :rtype: object
        """
        return self._account_sweep_initiate_action_record

    @account_sweep_initiate_action_record.setter
    def account_sweep_initiate_action_record(self, account_sweep_initiate_action_record):
        """Sets the account_sweep_initiate_action_record of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param account_sweep_initiate_action_record: The account_sweep_initiate_action_record of this BQAccountSweepInitiateOutputModel.
        :type account_sweep_initiate_action_record: object
        """

        self._account_sweep_initiate_action_record = account_sweep_initiate_action_record

    @property
    def account_sweep_instance_status(self):
        """Gets the account_sweep_instance_status of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Account Sweep instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The account_sweep_instance_status of this BQAccountSweepInitiateOutputModel.
        :rtype: str
        """
        return self._account_sweep_instance_status

    @account_sweep_instance_status.setter
    def account_sweep_instance_status(self, account_sweep_instance_status):
        """Sets the account_sweep_instance_status of this BQAccountSweepInitiateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Account Sweep instance (e.g. initialised, pending, active)   # noqa: E501

        :param account_sweep_instance_status: The account_sweep_instance_status of this BQAccountSweepInitiateOutputModel.
        :type account_sweep_instance_status: str
        """

        self._account_sweep_instance_status = account_sweep_instance_status

    @property
    def account_sweep_instance_record(self):
        """Gets the account_sweep_instance_record of this BQAccountSweepInitiateOutputModel.


        :return: The account_sweep_instance_record of this BQAccountSweepInitiateOutputModel.
        :rtype: InlineResponse2014AccountSweepInstanceRecord
        """
        return self._account_sweep_instance_record

    @account_sweep_instance_record.setter
    def account_sweep_instance_record(self, account_sweep_instance_record):
        """Sets the account_sweep_instance_record of this BQAccountSweepInitiateOutputModel.


        :param account_sweep_instance_record: The account_sweep_instance_record of this BQAccountSweepInitiateOutputModel.
        :type account_sweep_instance_record: InlineResponse2014AccountSweepInstanceRecord
        """

        self._account_sweep_instance_record = account_sweep_instance_record
