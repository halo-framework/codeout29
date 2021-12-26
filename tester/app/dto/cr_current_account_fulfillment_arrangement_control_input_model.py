# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_control_current_account_fulfillment_arrangement_control_action_request import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_control_current_account_fulfillment_arrangement_control_action_request import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest  # noqa: E501



class CRCurrentAccountFulfillmentArrangementControlInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_servicing_session_reference=None, current_account_fulfillment_arrangement_instance_reference=None, current_account_fulfillment_arrangement_control_action_task_record=None, current_account_fulfillment_arrangement_control_action_request=None):  # noqa: E501
        """CRCurrentAccountFulfillmentArrangementControlInputModel - a model defined in OpenAPI

        :param current_account_servicing_session_reference: The current_account_servicing_session_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.  # noqa: E501
        :type current_account_servicing_session_reference: str
        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param current_account_fulfillment_arrangement_control_action_task_record: The current_account_fulfillment_arrangement_control_action_task_record of this CRCurrentAccountFulfillmentArrangementControlInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_control_action_task_record: object
        :param current_account_fulfillment_arrangement_control_action_request: The current_account_fulfillment_arrangement_control_action_request of this CRCurrentAccountFulfillmentArrangementControlInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_control_action_request: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest
        """
        self.openapi_types = {
            'current_account_servicing_session_reference': str,
            'current_account_fulfillment_arrangement_instance_reference': str,
            'current_account_fulfillment_arrangement_control_action_task_record': object,
            'current_account_fulfillment_arrangement_control_action_request': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest
        }

        self.attribute_map = {
            'current_account_servicing_session_reference': 'currentAccountServicingSessionReference',
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'current_account_fulfillment_arrangement_control_action_task_record': 'currentAccountFulfillmentArrangementControlActionTaskRecord',
            'current_account_fulfillment_arrangement_control_action_request': 'currentAccountFulfillmentArrangementControlActionRequest'
        }

        self._current_account_servicing_session_reference = current_account_servicing_session_reference
        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._current_account_fulfillment_arrangement_control_action_task_record = current_account_fulfillment_arrangement_control_action_task_record
        self._current_account_fulfillment_arrangement_control_action_request = current_account_fulfillment_arrangement_control_action_request

    @classmethod
    def from_dict(cls, dikt) -> 'CRCurrentAccountFulfillmentArrangementControlInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CRCurrentAccountFulfillmentArrangementControlInputModel of this CRCurrentAccountFulfillmentArrangementControlInputModel.  # noqa: E501
        :rtype: CRCurrentAccountFulfillmentArrangementControlInputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_servicing_session_reference(self):
        """Gets the current_account_servicing_session_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the active servicing session   # noqa: E501

        :return: The current_account_servicing_session_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :rtype: str
        """
        return self._current_account_servicing_session_reference

    @current_account_servicing_session_reference.setter
    def current_account_servicing_session_reference(self, current_account_servicing_session_reference):
        """Sets the current_account_servicing_session_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the active servicing session   # noqa: E501

        :param current_account_servicing_session_reference: The current_account_servicing_session_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :type current_account_servicing_session_reference: str
        """

        self._current_account_servicing_session_reference = current_account_servicing_session_reference

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def current_account_fulfillment_arrangement_control_action_task_record(self):
        """Gets the current_account_fulfillment_arrangement_control_action_task_record of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The processing control service call consolidated processing record   # noqa: E501

        :return: The current_account_fulfillment_arrangement_control_action_task_record of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :rtype: object
        """
        return self._current_account_fulfillment_arrangement_control_action_task_record

    @current_account_fulfillment_arrangement_control_action_task_record.setter
    def current_account_fulfillment_arrangement_control_action_task_record(self, current_account_fulfillment_arrangement_control_action_task_record):
        """Sets the current_account_fulfillment_arrangement_control_action_task_record of this CRCurrentAccountFulfillmentArrangementControlInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The processing control service call consolidated processing record   # noqa: E501

        :param current_account_fulfillment_arrangement_control_action_task_record: The current_account_fulfillment_arrangement_control_action_task_record of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :type current_account_fulfillment_arrangement_control_action_task_record: object
        """

        self._current_account_fulfillment_arrangement_control_action_task_record = current_account_fulfillment_arrangement_control_action_task_record

    @property
    def current_account_fulfillment_arrangement_control_action_request(self):
        """Gets the current_account_fulfillment_arrangement_control_action_request of this CRCurrentAccountFulfillmentArrangementControlInputModel.


        :return: The current_account_fulfillment_arrangement_control_action_request of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest
        """
        return self._current_account_fulfillment_arrangement_control_action_request

    @current_account_fulfillment_arrangement_control_action_request.setter
    def current_account_fulfillment_arrangement_control_action_request(self, current_account_fulfillment_arrangement_control_action_request):
        """Sets the current_account_fulfillment_arrangement_control_action_request of this CRCurrentAccountFulfillmentArrangementControlInputModel.


        :param current_account_fulfillment_arrangement_control_action_request: The current_account_fulfillment_arrangement_control_action_request of this CRCurrentAccountFulfillmentArrangementControlInputModel.
        :type current_account_fulfillment_arrangement_control_action_request: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdControlCurrentAccountFulfillmentArrangementControlActionRequest
        """

        self._current_account_fulfillment_arrangement_control_action_request = current_account_fulfillment_arrangement_control_action_request
