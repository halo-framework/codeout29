# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2012_current_account_fulfillment_arrangement_instance_record import InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
from tester.app.dto.inline_response2012_service_fees_instance_record import InlineResponse2012ServiceFeesInstanceRecord
from tester import util

from tester.app.dto.inline_response2012_current_account_fulfillment_arrangement_instance_record import InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501
from tester.app.dto.inline_response2012_service_fees_instance_record import InlineResponse2012ServiceFeesInstanceRecord  # noqa: E501



class InlineResponse2012(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, service_fees_instance_reference=None, service_fees_initiate_action_reference=None, service_fees_initiate_action_record=None, service_fees_instance_status=None, service_fees_instance_record=None):  # noqa: E501
        """InlineResponse2012 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2012.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        :param service_fees_instance_reference: The service_fees_instance_reference of this InlineResponse2012.  # noqa: E501
        :type service_fees_instance_reference: str
        :param service_fees_initiate_action_reference: The service_fees_initiate_action_reference of this InlineResponse2012.  # noqa: E501
        :type service_fees_initiate_action_reference: str
        :param service_fees_initiate_action_record: The service_fees_initiate_action_record of this InlineResponse2012.  # noqa: E501
        :type service_fees_initiate_action_record: object
        :param service_fees_instance_status: The service_fees_instance_status of this InlineResponse2012.  # noqa: E501
        :type service_fees_instance_status: str
        :param service_fees_instance_record: The service_fees_instance_record of this InlineResponse2012.  # noqa: E501
        :type service_fees_instance_record: InlineResponse2012ServiceFeesInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord,
            'service_fees_instance_reference': str,
            'service_fees_initiate_action_reference': str,
            'service_fees_initiate_action_record': object,
            'service_fees_instance_status': str,
            'service_fees_instance_record': InlineResponse2012ServiceFeesInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'service_fees_instance_reference': 'serviceFeesInstanceReference',
            'service_fees_initiate_action_reference': 'serviceFeesInitiateActionReference',
            'service_fees_initiate_action_record': 'serviceFeesInitiateActionRecord',
            'service_fees_instance_status': 'serviceFeesInstanceStatus',
            'service_fees_instance_record': 'serviceFeesInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._service_fees_instance_reference = service_fees_instance_reference
        self._service_fees_initiate_action_reference = service_fees_initiate_action_reference
        self._service_fees_initiate_action_record = service_fees_initiate_action_record
        self._service_fees_instance_status = service_fees_instance_status
        self._service_fees_instance_record = service_fees_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2012':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_2 of this InlineResponse2012.  # noqa: E501
        :rtype: InlineResponse2012
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2012.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2012.
        :rtype: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2012.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2012.
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2012CurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def service_fees_instance_reference(self):
        """Gets the service_fees_instance_reference of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Service Fees instance   # noqa: E501

        :return: The service_fees_instance_reference of this InlineResponse2012.
        :rtype: str
        """
        return self._service_fees_instance_reference

    @service_fees_instance_reference.setter
    def service_fees_instance_reference(self, service_fees_instance_reference):
        """Sets the service_fees_instance_reference of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Service Fees instance   # noqa: E501

        :param service_fees_instance_reference: The service_fees_instance_reference of this InlineResponse2012.
        :type service_fees_instance_reference: str
        """

        self._service_fees_instance_reference = service_fees_instance_reference

    @property
    def service_fees_initiate_action_reference(self):
        """Gets the service_fees_initiate_action_reference of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :return: The service_fees_initiate_action_reference of this InlineResponse2012.
        :rtype: str
        """
        return self._service_fees_initiate_action_reference

    @service_fees_initiate_action_reference.setter
    def service_fees_initiate_action_reference(self, service_fees_initiate_action_reference):
        """Sets the service_fees_initiate_action_reference of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :param service_fees_initiate_action_reference: The service_fees_initiate_action_reference of this InlineResponse2012.
        :type service_fees_initiate_action_reference: str
        """

        self._service_fees_initiate_action_reference = service_fees_initiate_action_reference

    @property
    def service_fees_initiate_action_record(self):
        """Gets the service_fees_initiate_action_record of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The service_fees_initiate_action_record of this InlineResponse2012.
        :rtype: object
        """
        return self._service_fees_initiate_action_record

    @service_fees_initiate_action_record.setter
    def service_fees_initiate_action_record(self, service_fees_initiate_action_record):
        """Sets the service_fees_initiate_action_record of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param service_fees_initiate_action_record: The service_fees_initiate_action_record of this InlineResponse2012.
        :type service_fees_initiate_action_record: object
        """

        self._service_fees_initiate_action_record = service_fees_initiate_action_record

    @property
    def service_fees_instance_status(self):
        """Gets the service_fees_instance_status of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Service Fees instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The service_fees_instance_status of this InlineResponse2012.
        :rtype: str
        """
        return self._service_fees_instance_status

    @service_fees_instance_status.setter
    def service_fees_instance_status(self, service_fees_instance_status):
        """Sets the service_fees_instance_status of this InlineResponse2012.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Service Fees instance (e.g. initialised, pending, active)   # noqa: E501

        :param service_fees_instance_status: The service_fees_instance_status of this InlineResponse2012.
        :type service_fees_instance_status: str
        """

        self._service_fees_instance_status = service_fees_instance_status

    @property
    def service_fees_instance_record(self):
        """Gets the service_fees_instance_record of this InlineResponse2012.


        :return: The service_fees_instance_record of this InlineResponse2012.
        :rtype: InlineResponse2012ServiceFeesInstanceRecord
        """
        return self._service_fees_instance_record

    @service_fees_instance_record.setter
    def service_fees_instance_record(self, service_fees_instance_record):
        """Sets the service_fees_instance_record of this InlineResponse2012.


        :param service_fees_instance_record: The service_fees_instance_record of this InlineResponse2012.
        :type service_fees_instance_record: InlineResponse2012ServiceFeesInstanceRecord
        """

        self._service_fees_instance_record = service_fees_instance_record
