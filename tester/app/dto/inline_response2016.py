# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2016_current_account_fulfillment_arrangement_instance_record import InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord
from tester.app.dto.inline_response2016_payments_instance_record import InlineResponse2016PaymentsInstanceRecord
from tester import util

from tester.app.dto.inline_response2016_current_account_fulfillment_arrangement_instance_record import InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501
from tester.app.dto.inline_response2016_payments_instance_record import InlineResponse2016PaymentsInstanceRecord  # noqa: E501



class InlineResponse2016(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, payments_instance_reference=None, payments_initiate_action_reference=None, payments_initiate_action_record=None, payments_instance_status=None, payments_instance_record=None):  # noqa: E501
        """InlineResponse2016 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2016.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord
        :param payments_instance_reference: The payments_instance_reference of this InlineResponse2016.  # noqa: E501
        :type payments_instance_reference: str
        :param payments_initiate_action_reference: The payments_initiate_action_reference of this InlineResponse2016.  # noqa: E501
        :type payments_initiate_action_reference: str
        :param payments_initiate_action_record: The payments_initiate_action_record of this InlineResponse2016.  # noqa: E501
        :type payments_initiate_action_record: object
        :param payments_instance_status: The payments_instance_status of this InlineResponse2016.  # noqa: E501
        :type payments_instance_status: str
        :param payments_instance_record: The payments_instance_record of this InlineResponse2016.  # noqa: E501
        :type payments_instance_record: InlineResponse2016PaymentsInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord,
            'payments_instance_reference': str,
            'payments_initiate_action_reference': str,
            'payments_initiate_action_record': object,
            'payments_instance_status': str,
            'payments_instance_record': InlineResponse2016PaymentsInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'payments_instance_reference': 'paymentsInstanceReference',
            'payments_initiate_action_reference': 'paymentsInitiateActionReference',
            'payments_initiate_action_record': 'paymentsInitiateActionRecord',
            'payments_instance_status': 'paymentsInstanceStatus',
            'payments_instance_record': 'paymentsInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._payments_instance_reference = payments_instance_reference
        self._payments_initiate_action_reference = payments_initiate_action_reference
        self._payments_initiate_action_record = payments_initiate_action_record
        self._payments_instance_status = payments_instance_status
        self._payments_instance_record = payments_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2016':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_6 of this InlineResponse2016.  # noqa: E501
        :rtype: InlineResponse2016
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2016.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2016.
        :rtype: InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2016.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2016.
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2016CurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def payments_instance_reference(self):
        """Gets the payments_instance_reference of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :return: The payments_instance_reference of this InlineResponse2016.
        :rtype: str
        """
        return self._payments_instance_reference

    @payments_instance_reference.setter
    def payments_instance_reference(self, payments_instance_reference):
        """Sets the payments_instance_reference of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :param payments_instance_reference: The payments_instance_reference of this InlineResponse2016.
        :type payments_instance_reference: str
        """

        self._payments_instance_reference = payments_instance_reference

    @property
    def payments_initiate_action_reference(self):
        """Gets the payments_initiate_action_reference of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :return: The payments_initiate_action_reference of this InlineResponse2016.
        :rtype: str
        """
        return self._payments_initiate_action_reference

    @payments_initiate_action_reference.setter
    def payments_initiate_action_reference(self, payments_initiate_action_reference):
        """Sets the payments_initiate_action_reference of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :param payments_initiate_action_reference: The payments_initiate_action_reference of this InlineResponse2016.
        :type payments_initiate_action_reference: str
        """

        self._payments_initiate_action_reference = payments_initiate_action_reference

    @property
    def payments_initiate_action_record(self):
        """Gets the payments_initiate_action_record of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The payments_initiate_action_record of this InlineResponse2016.
        :rtype: object
        """
        return self._payments_initiate_action_record

    @payments_initiate_action_record.setter
    def payments_initiate_action_record(self, payments_initiate_action_record):
        """Sets the payments_initiate_action_record of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param payments_initiate_action_record: The payments_initiate_action_record of this InlineResponse2016.
        :type payments_initiate_action_record: object
        """

        self._payments_initiate_action_record = payments_initiate_action_record

    @property
    def payments_instance_status(self):
        """Gets the payments_instance_status of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Payments instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The payments_instance_status of this InlineResponse2016.
        :rtype: str
        """
        return self._payments_instance_status

    @payments_instance_status.setter
    def payments_instance_status(self, payments_instance_status):
        """Sets the payments_instance_status of this InlineResponse2016.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Payments instance (e.g. initialised, pending, active)   # noqa: E501

        :param payments_instance_status: The payments_instance_status of this InlineResponse2016.
        :type payments_instance_status: str
        """

        self._payments_instance_status = payments_instance_status

    @property
    def payments_instance_record(self):
        """Gets the payments_instance_record of this InlineResponse2016.


        :return: The payments_instance_record of this InlineResponse2016.
        :rtype: InlineResponse2016PaymentsInstanceRecord
        """
        return self._payments_instance_record

    @payments_instance_record.setter
    def payments_instance_record(self, payments_instance_record):
        """Sets the payments_instance_record of this InlineResponse2016.


        :param payments_instance_record: The payments_instance_record of this InlineResponse2016.
        :type payments_instance_record: InlineResponse2016PaymentsInstanceRecord
        """

        self._payments_instance_record = payments_instance_record
