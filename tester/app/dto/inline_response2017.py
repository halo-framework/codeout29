# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2017_current_account_fulfillment_arrangement_instance_record import InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord
from tester.app.dto.inline_response2017_issued_device_instance_record import InlineResponse2017IssuedDeviceInstanceRecord
from tester import util

from tester.app.dto.inline_response2017_current_account_fulfillment_arrangement_instance_record import InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501
from tester.app.dto.inline_response2017_issued_device_instance_record import InlineResponse2017IssuedDeviceInstanceRecord  # noqa: E501



class InlineResponse2017(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, issued_device_instance_reference=None, issued_device_initiate_action_reference=None, issued_device_initiate_action_record=None, issued_device_instance_status=None, issued_device_instance_record=None):  # noqa: E501
        """InlineResponse2017 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2017.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord
        :param issued_device_instance_reference: The issued_device_instance_reference of this InlineResponse2017.  # noqa: E501
        :type issued_device_instance_reference: str
        :param issued_device_initiate_action_reference: The issued_device_initiate_action_reference of this InlineResponse2017.  # noqa: E501
        :type issued_device_initiate_action_reference: str
        :param issued_device_initiate_action_record: The issued_device_initiate_action_record of this InlineResponse2017.  # noqa: E501
        :type issued_device_initiate_action_record: object
        :param issued_device_instance_status: The issued_device_instance_status of this InlineResponse2017.  # noqa: E501
        :type issued_device_instance_status: str
        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse2017.  # noqa: E501
        :type issued_device_instance_record: InlineResponse2017IssuedDeviceInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord,
            'issued_device_instance_reference': str,
            'issued_device_initiate_action_reference': str,
            'issued_device_initiate_action_record': object,
            'issued_device_instance_status': str,
            'issued_device_instance_record': InlineResponse2017IssuedDeviceInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'issued_device_instance_reference': 'issuedDeviceInstanceReference',
            'issued_device_initiate_action_reference': 'issuedDeviceInitiateActionReference',
            'issued_device_initiate_action_record': 'issuedDeviceInitiateActionRecord',
            'issued_device_instance_status': 'issuedDeviceInstanceStatus',
            'issued_device_instance_record': 'issuedDeviceInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._issued_device_instance_reference = issued_device_instance_reference
        self._issued_device_initiate_action_reference = issued_device_initiate_action_reference
        self._issued_device_initiate_action_record = issued_device_initiate_action_record
        self._issued_device_instance_status = issued_device_instance_status
        self._issued_device_instance_record = issued_device_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2017':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_7 of this InlineResponse2017.  # noqa: E501
        :rtype: InlineResponse2017
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2017.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2017.
        :rtype: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineResponse2017.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineResponse2017.
        :type current_account_fulfillment_arrangement_instance_record: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def issued_device_instance_reference(self):
        """Gets the issued_device_instance_reference of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Issued Device instance   # noqa: E501

        :return: The issued_device_instance_reference of this InlineResponse2017.
        :rtype: str
        """
        return self._issued_device_instance_reference

    @issued_device_instance_reference.setter
    def issued_device_instance_reference(self, issued_device_instance_reference):
        """Sets the issued_device_instance_reference of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Issued Device instance   # noqa: E501

        :param issued_device_instance_reference: The issued_device_instance_reference of this InlineResponse2017.
        :type issued_device_instance_reference: str
        """

        self._issued_device_instance_reference = issued_device_instance_reference

    @property
    def issued_device_initiate_action_reference(self):
        """Gets the issued_device_initiate_action_reference of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :return: The issued_device_initiate_action_reference of this InlineResponse2017.
        :rtype: str
        """
        return self._issued_device_initiate_action_reference

    @issued_device_initiate_action_reference.setter
    def issued_device_initiate_action_reference(self, issued_device_initiate_action_reference):
        """Sets the issued_device_initiate_action_reference of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an Initiate service call   # noqa: E501

        :param issued_device_initiate_action_reference: The issued_device_initiate_action_reference of this InlineResponse2017.
        :type issued_device_initiate_action_reference: str
        """

        self._issued_device_initiate_action_reference = issued_device_initiate_action_reference

    @property
    def issued_device_initiate_action_record(self):
        """Gets the issued_device_initiate_action_record of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The issued_device_initiate_action_record of this InlineResponse2017.
        :rtype: object
        """
        return self._issued_device_initiate_action_record

    @issued_device_initiate_action_record.setter
    def issued_device_initiate_action_record(self, issued_device_initiate_action_record):
        """Sets the issued_device_initiate_action_record of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param issued_device_initiate_action_record: The issued_device_initiate_action_record of this InlineResponse2017.
        :type issued_device_initiate_action_record: object
        """

        self._issued_device_initiate_action_record = issued_device_initiate_action_record

    @property
    def issued_device_instance_status(self):
        """Gets the issued_device_instance_status of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Issued Device instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The issued_device_instance_status of this InlineResponse2017.
        :rtype: str
        """
        return self._issued_device_instance_status

    @issued_device_instance_status.setter
    def issued_device_instance_status(self, issued_device_instance_status):
        """Sets the issued_device_instance_status of this InlineResponse2017.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Issued Device instance (e.g. initialised, pending, active)   # noqa: E501

        :param issued_device_instance_status: The issued_device_instance_status of this InlineResponse2017.
        :type issued_device_instance_status: str
        """

        self._issued_device_instance_status = issued_device_instance_status

    @property
    def issued_device_instance_record(self):
        """Gets the issued_device_instance_record of this InlineResponse2017.


        :return: The issued_device_instance_record of this InlineResponse2017.
        :rtype: InlineResponse2017IssuedDeviceInstanceRecord
        """
        return self._issued_device_instance_record

    @issued_device_instance_record.setter
    def issued_device_instance_record(self, issued_device_instance_record):
        """Sets the issued_device_instance_record of this InlineResponse2017.


        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse2017.
        :type issued_device_instance_record: InlineResponse2017IssuedDeviceInstanceRecord
        """

        self._issued_device_instance_record = issued_device_instance_record
