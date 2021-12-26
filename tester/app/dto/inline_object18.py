# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_update_payments_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_update_payments_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord  # noqa: E501



class InlineObject18(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_reference=None, payments_instance_reference=None, payments_instance_record=None, payments_update_action_task_record=None, payments_update_action_request=None):  # noqa: E501
        """InlineObject18 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject18.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param payments_instance_reference: The payments_instance_reference of this InlineObject18.  # noqa: E501
        :type payments_instance_reference: str
        :param payments_instance_record: The payments_instance_record of this InlineObject18.  # noqa: E501
        :type payments_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord
        :param payments_update_action_task_record: The payments_update_action_task_record of this InlineObject18.  # noqa: E501
        :type payments_update_action_task_record: object
        :param payments_update_action_request: The payments_update_action_request of this InlineObject18.  # noqa: E501
        :type payments_update_action_request: str
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_reference': str,
            'payments_instance_reference': str,
            'payments_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord,
            'payments_update_action_task_record': object,
            'payments_update_action_request': str
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'payments_instance_reference': 'paymentsInstanceReference',
            'payments_instance_record': 'paymentsInstanceRecord',
            'payments_update_action_task_record': 'paymentsUpdateActionTaskRecord',
            'payments_update_action_request': 'paymentsUpdateActionRequest'
        }

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._payments_instance_reference = payments_instance_reference
        self._payments_instance_record = payments_instance_record
        self._payments_update_action_task_record = payments_update_action_task_record
        self._payments_update_action_request = payments_update_action_request

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject18':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_18 of this InlineObject18.  # noqa: E501
        :rtype: InlineObject18
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this InlineObject18.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject18.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def payments_instance_reference(self):
        """Gets the payments_instance_reference of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :return: The payments_instance_reference of this InlineObject18.
        :rtype: str
        """
        return self._payments_instance_reference

    @payments_instance_reference.setter
    def payments_instance_reference(self, payments_instance_reference):
        """Sets the payments_instance_reference of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :param payments_instance_reference: The payments_instance_reference of this InlineObject18.
        :type payments_instance_reference: str
        """

        self._payments_instance_reference = payments_instance_reference

    @property
    def payments_instance_record(self):
        """Gets the payments_instance_record of this InlineObject18.


        :return: The payments_instance_record of this InlineObject18.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord
        """
        return self._payments_instance_record

    @payments_instance_record.setter
    def payments_instance_record(self, payments_instance_record):
        """Sets the payments_instance_record of this InlineObject18.


        :param payments_instance_record: The payments_instance_record of this InlineObject18.
        :type payments_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdUpdatePaymentsInstanceRecord
        """

        self._payments_instance_record = payments_instance_record

    @property
    def payments_update_action_task_record(self):
        """Gets the payments_update_action_task_record of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The payments_update_action_task_record of this InlineObject18.
        :rtype: object
        """
        return self._payments_update_action_task_record

    @payments_update_action_task_record.setter
    def payments_update_action_task_record(self, payments_update_action_task_record):
        """Sets the payments_update_action_task_record of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param payments_update_action_task_record: The payments_update_action_task_record of this InlineObject18.
        :type payments_update_action_task_record: object
        """

        self._payments_update_action_task_record = payments_update_action_task_record

    @property
    def payments_update_action_request(self):
        """Gets the payments_update_action_request of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :return: The payments_update_action_request of this InlineObject18.
        :rtype: str
        """
        return self._payments_update_action_request

    @payments_update_action_request.setter
    def payments_update_action_request(self, payments_update_action_request):
        """Sets the payments_update_action_request of this InlineObject18.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :param payments_update_action_request: The payments_update_action_request of this InlineObject18.
        :type payments_update_action_request: str
        """

        self._payments_update_action_request = payments_update_action_request
