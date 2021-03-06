# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501



class InlineObject3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_servicing_session_reference=None, current_account_fulfillment_arrangement_initiate_action_record=None, current_account_fulfillment_arrangement_instance_status=None, current_account_fulfillment_arrangement_instance_record=None):  # noqa: E501
        """InlineObject3 - a model defined in OpenAPI

        :param current_account_servicing_session_reference: The current_account_servicing_session_reference of this InlineObject3.  # noqa: E501
        :type current_account_servicing_session_reference: str
        :param current_account_fulfillment_arrangement_initiate_action_record: The current_account_fulfillment_arrangement_initiate_action_record of this InlineObject3.  # noqa: E501
        :type current_account_fulfillment_arrangement_initiate_action_record: object
        :param current_account_fulfillment_arrangement_instance_status: The current_account_fulfillment_arrangement_instance_status of this InlineObject3.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_status: str
        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineObject3.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """
        self.openapi_types = {
            'current_account_servicing_session_reference': str,
            'current_account_fulfillment_arrangement_initiate_action_record': object,
            'current_account_fulfillment_arrangement_instance_status': str,
            'current_account_fulfillment_arrangement_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        }

        self.attribute_map = {
            'current_account_servicing_session_reference': 'currentAccountServicingSessionReference',
            'current_account_fulfillment_arrangement_initiate_action_record': 'currentAccountFulfillmentArrangementInitiateActionRecord',
            'current_account_fulfillment_arrangement_instance_status': 'currentAccountFulfillmentArrangementInstanceStatus',
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord'
        }

        self._current_account_servicing_session_reference = current_account_servicing_session_reference
        self._current_account_fulfillment_arrangement_initiate_action_record = current_account_fulfillment_arrangement_initiate_action_record
        self._current_account_fulfillment_arrangement_instance_status = current_account_fulfillment_arrangement_instance_status
        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject3':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_3 of this InlineObject3.  # noqa: E501
        :rtype: InlineObject3
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_servicing_session_reference(self):
        """Gets the current_account_servicing_session_reference of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the active servicing session   # noqa: E501

        :return: The current_account_servicing_session_reference of this InlineObject3.
        :rtype: str
        """
        return self._current_account_servicing_session_reference

    @current_account_servicing_session_reference.setter
    def current_account_servicing_session_reference(self, current_account_servicing_session_reference):
        """Sets the current_account_servicing_session_reference of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the active servicing session   # noqa: E501

        :param current_account_servicing_session_reference: The current_account_servicing_session_reference of this InlineObject3.
        :type current_account_servicing_session_reference: str
        """

        self._current_account_servicing_session_reference = current_account_servicing_session_reference

    @property
    def current_account_fulfillment_arrangement_initiate_action_record(self):
        """Gets the current_account_fulfillment_arrangement_initiate_action_record of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The current_account_fulfillment_arrangement_initiate_action_record of this InlineObject3.
        :rtype: object
        """
        return self._current_account_fulfillment_arrangement_initiate_action_record

    @current_account_fulfillment_arrangement_initiate_action_record.setter
    def current_account_fulfillment_arrangement_initiate_action_record(self, current_account_fulfillment_arrangement_initiate_action_record):
        """Sets the current_account_fulfillment_arrangement_initiate_action_record of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param current_account_fulfillment_arrangement_initiate_action_record: The current_account_fulfillment_arrangement_initiate_action_record of this InlineObject3.
        :type current_account_fulfillment_arrangement_initiate_action_record: object
        """

        self._current_account_fulfillment_arrangement_initiate_action_record = current_account_fulfillment_arrangement_initiate_action_record

    @property
    def current_account_fulfillment_arrangement_instance_status(self):
        """Gets the current_account_fulfillment_arrangement_instance_status of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Current Account Fulfillment Arrangement instance (e.g. initialised, pending, active)   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_status of this InlineObject3.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_status

    @current_account_fulfillment_arrangement_instance_status.setter
    def current_account_fulfillment_arrangement_instance_status(self, current_account_fulfillment_arrangement_instance_status):
        """Sets the current_account_fulfillment_arrangement_instance_status of this InlineObject3.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the Current Account Fulfillment Arrangement instance (e.g. initialised, pending, active)   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_status: The current_account_fulfillment_arrangement_instance_status of this InlineObject3.
        :type current_account_fulfillment_arrangement_instance_status: str
        """

        self._current_account_fulfillment_arrangement_instance_status = current_account_fulfillment_arrangement_instance_status

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineObject3.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineObject3.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineObject3.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineObject3.
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
