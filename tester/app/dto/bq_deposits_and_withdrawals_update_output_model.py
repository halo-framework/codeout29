# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_bq_reference_id_update_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_bq_reference_id_update_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord  # noqa: E501



class BQDepositsAndWithdrawalsUpdateOutputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposits_and_withdrawals_instance_record=None, deposits_and_withdrawals_update_action_task_reference=None, deposits_and_withdrawals_update_action_task_record=None, update_response_record=None):  # noqa: E501
        """BQDepositsAndWithdrawalsUpdateOutputModel - a model defined in OpenAPI

        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsUpdateOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        :param deposits_and_withdrawals_update_action_task_reference: The deposits_and_withdrawals_update_action_task_reference of this BQDepositsAndWithdrawalsUpdateOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_update_action_task_reference: str
        :param deposits_and_withdrawals_update_action_task_record: The deposits_and_withdrawals_update_action_task_record of this BQDepositsAndWithdrawalsUpdateOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_update_action_task_record: object
        :param update_response_record: The update_response_record of this BQDepositsAndWithdrawalsUpdateOutputModel.  # noqa: E501
        :type update_response_record: object
        """
        self.openapi_types = {
            'deposits_and_withdrawals_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord,
            'deposits_and_withdrawals_update_action_task_reference': str,
            'deposits_and_withdrawals_update_action_task_record': object,
            'update_response_record': object
        }

        self.attribute_map = {
            'deposits_and_withdrawals_instance_record': 'depositsAndWithdrawalsInstanceRecord',
            'deposits_and_withdrawals_update_action_task_reference': 'depositsAndWithdrawalsUpdateActionTaskReference',
            'deposits_and_withdrawals_update_action_task_record': 'depositsAndWithdrawalsUpdateActionTaskRecord',
            'update_response_record': 'updateResponseRecord'
        }

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record
        self._deposits_and_withdrawals_update_action_task_reference = deposits_and_withdrawals_update_action_task_reference
        self._deposits_and_withdrawals_update_action_task_record = deposits_and_withdrawals_update_action_task_record
        self._update_response_record = update_response_record

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsUpdateOutputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsUpdateOutputModel of this BQDepositsAndWithdrawalsUpdateOutputModel.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsUpdateOutputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposits_and_withdrawals_instance_record(self):
        """Gets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsUpdateOutputModel.


        :return: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        """
        return self._deposits_and_withdrawals_instance_record

    @deposits_and_withdrawals_instance_record.setter
    def deposits_and_withdrawals_instance_record(self, deposits_and_withdrawals_instance_record):
        """Sets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsUpdateOutputModel.


        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdUpdateDepositsAndWithdrawalsInstanceRecord
        """

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record

    @property
    def deposits_and_withdrawals_update_action_task_reference(self):
        """Gets the deposits_and_withdrawals_update_action_task_reference of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :return: The deposits_and_withdrawals_update_action_task_reference of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :rtype: str
        """
        return self._deposits_and_withdrawals_update_action_task_reference

    @deposits_and_withdrawals_update_action_task_reference.setter
    def deposits_and_withdrawals_update_action_task_reference(self, deposits_and_withdrawals_update_action_task_reference):
        """Sets the deposits_and_withdrawals_update_action_task_reference of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :param deposits_and_withdrawals_update_action_task_reference: The deposits_and_withdrawals_update_action_task_reference of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :type deposits_and_withdrawals_update_action_task_reference: str
        """

        self._deposits_and_withdrawals_update_action_task_reference = deposits_and_withdrawals_update_action_task_reference

    @property
    def deposits_and_withdrawals_update_action_task_record(self):
        """Gets the deposits_and_withdrawals_update_action_task_record of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The deposits_and_withdrawals_update_action_task_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :rtype: object
        """
        return self._deposits_and_withdrawals_update_action_task_record

    @deposits_and_withdrawals_update_action_task_record.setter
    def deposits_and_withdrawals_update_action_task_record(self, deposits_and_withdrawals_update_action_task_record):
        """Sets the deposits_and_withdrawals_update_action_task_record of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param deposits_and_withdrawals_update_action_task_record: The deposits_and_withdrawals_update_action_task_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :type deposits_and_withdrawals_update_action_task_record: object
        """

        self._deposits_and_withdrawals_update_action_task_record = deposits_and_withdrawals_update_action_task_record

    @property
    def update_response_record(self):
        """Gets the update_response_record of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :return: The update_response_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :rtype: object
        """
        return self._update_response_record

    @update_response_record.setter
    def update_response_record(self, update_response_record):
        """Sets the update_response_record of this BQDepositsAndWithdrawalsUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :param update_response_record: The update_response_record of this BQDepositsAndWithdrawalsUpdateOutputModel.
        :type update_response_record: object
        """

        self._update_response_record = update_response_record
