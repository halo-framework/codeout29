# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_bq_reference_id_update_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_bq_reference_id_update_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord  # noqa: E501



class InlineObject15(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_reference=None, deposits_and_withdrawals_instance_reference=None, deposits_and_withdrawals_instance_record=None, deposits_and_withdrawals_update_action_task_record=None, deposits_and_withdrawals_update_action_request=None):  # noqa: E501
        """InlineObject15 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject15.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param deposits_and_withdrawals_instance_reference: The deposits_and_withdrawals_instance_reference of this InlineObject15.  # noqa: E501
        :type deposits_and_withdrawals_instance_reference: str
        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this InlineObject15.  # noqa: E501
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        :param deposits_and_withdrawals_update_action_task_record: The deposits_and_withdrawals_update_action_task_record of this InlineObject15.  # noqa: E501
        :type deposits_and_withdrawals_update_action_task_record: object
        :param deposits_and_withdrawals_update_action_request: The deposits_and_withdrawals_update_action_request of this InlineObject15.  # noqa: E501
        :type deposits_and_withdrawals_update_action_request: str
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_reference': str,
            'deposits_and_withdrawals_instance_reference': str,
            'deposits_and_withdrawals_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord,
            'deposits_and_withdrawals_update_action_task_record': object,
            'deposits_and_withdrawals_update_action_request': str
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'deposits_and_withdrawals_instance_reference': 'depositsAndWithdrawalsInstanceReference',
            'deposits_and_withdrawals_instance_record': 'depositsAndWithdrawalsInstanceRecord',
            'deposits_and_withdrawals_update_action_task_record': 'depositsAndWithdrawalsUpdateActionTaskRecord',
            'deposits_and_withdrawals_update_action_request': 'depositsAndWithdrawalsUpdateActionRequest'
        }

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._deposits_and_withdrawals_instance_reference = deposits_and_withdrawals_instance_reference
        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record
        self._deposits_and_withdrawals_update_action_task_record = deposits_and_withdrawals_update_action_task_record
        self._deposits_and_withdrawals_update_action_request = deposits_and_withdrawals_update_action_request

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject15':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_15 of this InlineObject15.  # noqa: E501
        :rtype: InlineObject15
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this InlineObject15.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject15.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def deposits_and_withdrawals_instance_reference(self):
        """Gets the deposits_and_withdrawals_instance_reference of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Deposits And Withdrawals instance   # noqa: E501

        :return: The deposits_and_withdrawals_instance_reference of this InlineObject15.
        :rtype: str
        """
        return self._deposits_and_withdrawals_instance_reference

    @deposits_and_withdrawals_instance_reference.setter
    def deposits_and_withdrawals_instance_reference(self, deposits_and_withdrawals_instance_reference):
        """Sets the deposits_and_withdrawals_instance_reference of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Deposits And Withdrawals instance   # noqa: E501

        :param deposits_and_withdrawals_instance_reference: The deposits_and_withdrawals_instance_reference of this InlineObject15.
        :type deposits_and_withdrawals_instance_reference: str
        """

        self._deposits_and_withdrawals_instance_reference = deposits_and_withdrawals_instance_reference

    @property
    def deposits_and_withdrawals_instance_record(self):
        """Gets the deposits_and_withdrawals_instance_record of this InlineObject15.


        :return: The deposits_and_withdrawals_instance_record of this InlineObject15.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        """
        return self._deposits_and_withdrawals_instance_record

    @deposits_and_withdrawals_instance_record.setter
    def deposits_and_withdrawals_instance_record(self, deposits_and_withdrawals_instance_record):
        """Sets the deposits_and_withdrawals_instance_record of this InlineObject15.


        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this InlineObject15.
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        """

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record

    @property
    def deposits_and_withdrawals_update_action_task_record(self):
        """Gets the deposits_and_withdrawals_update_action_task_record of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The deposits_and_withdrawals_update_action_task_record of this InlineObject15.
        :rtype: object
        """
        return self._deposits_and_withdrawals_update_action_task_record

    @deposits_and_withdrawals_update_action_task_record.setter
    def deposits_and_withdrawals_update_action_task_record(self, deposits_and_withdrawals_update_action_task_record):
        """Sets the deposits_and_withdrawals_update_action_task_record of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param deposits_and_withdrawals_update_action_task_record: The deposits_and_withdrawals_update_action_task_record of this InlineObject15.
        :type deposits_and_withdrawals_update_action_task_record: object
        """

        self._deposits_and_withdrawals_update_action_task_record = deposits_and_withdrawals_update_action_task_record

    @property
    def deposits_and_withdrawals_update_action_request(self):
        """Gets the deposits_and_withdrawals_update_action_request of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :return: The deposits_and_withdrawals_update_action_request of this InlineObject15.
        :rtype: str
        """
        return self._deposits_and_withdrawals_update_action_request

    @deposits_and_withdrawals_update_action_request.setter
    def deposits_and_withdrawals_update_action_request(self, deposits_and_withdrawals_update_action_request):
        """Sets the deposits_and_withdrawals_update_action_request of this InlineObject15.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :param deposits_and_withdrawals_update_action_request: The deposits_and_withdrawals_update_action_request of this InlineObject15.
        :type deposits_and_withdrawals_update_action_request: str
        """

        self._deposits_and_withdrawals_update_action_request = deposits_and_withdrawals_update_action_request
