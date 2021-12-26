# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_initiation_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_depositsandwithdrawals_initiation_deposits_and_withdrawals_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord  # noqa: E501



class BQDepositsAndWithdrawalsInitiateInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, current_account_fulfillment_arrangement_instance_reference=None, deposits_and_withdrawals_initiate_action_record=None, deposits_and_withdrawals_instance_record=None):  # noqa: E501
        """BQDepositsAndWithdrawalsInitiateInputModel - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this BQDepositsAndWithdrawalsInitiateInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param deposits_and_withdrawals_initiate_action_record: The deposits_and_withdrawals_initiate_action_record of this BQDepositsAndWithdrawalsInitiateInputModel.  # noqa: E501
        :type deposits_and_withdrawals_initiate_action_record: object
        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.  # noqa: E501
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord,
            'current_account_fulfillment_arrangement_instance_reference': str,
            'deposits_and_withdrawals_initiate_action_record': object,
            'deposits_and_withdrawals_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'deposits_and_withdrawals_initiate_action_record': 'depositsAndWithdrawalsInitiateActionRecord',
            'deposits_and_withdrawals_instance_record': 'depositsAndWithdrawalsInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._deposits_and_withdrawals_initiate_action_record = deposits_and_withdrawals_initiate_action_record
        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsInitiateInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsInitiateInputModel of this BQDepositsAndWithdrawalsInitiateInputModel.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsInitiateInputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.


        :return: The current_account_fulfillment_arrangement_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this BQDepositsAndWithdrawalsInitiateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this BQDepositsAndWithdrawalsInitiateInputModel.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this BQDepositsAndWithdrawalsInitiateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this BQDepositsAndWithdrawalsInitiateInputModel.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def deposits_and_withdrawals_initiate_action_record(self):
        """Gets the deposits_and_withdrawals_initiate_action_record of this BQDepositsAndWithdrawalsInitiateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The deposits_and_withdrawals_initiate_action_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :rtype: object
        """
        return self._deposits_and_withdrawals_initiate_action_record

    @deposits_and_withdrawals_initiate_action_record.setter
    def deposits_and_withdrawals_initiate_action_record(self, deposits_and_withdrawals_initiate_action_record):
        """Sets the deposits_and_withdrawals_initiate_action_record of this BQDepositsAndWithdrawalsInitiateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param deposits_and_withdrawals_initiate_action_record: The deposits_and_withdrawals_initiate_action_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :type deposits_and_withdrawals_initiate_action_record: object
        """

        self._deposits_and_withdrawals_initiate_action_record = deposits_and_withdrawals_initiate_action_record

    @property
    def deposits_and_withdrawals_instance_record(self):
        """Gets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.


        :return: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
        """
        return self._deposits_and_withdrawals_instance_record

    @deposits_and_withdrawals_instance_record.setter
    def deposits_and_withdrawals_instance_record(self, deposits_and_withdrawals_instance_record):
        """Sets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.


        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsInitiateInputModel.
        :type deposits_and_withdrawals_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
        """

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record
