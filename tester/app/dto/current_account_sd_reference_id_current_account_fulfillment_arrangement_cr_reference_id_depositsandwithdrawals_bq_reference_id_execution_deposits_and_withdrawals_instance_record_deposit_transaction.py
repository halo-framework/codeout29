# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposit_transaction_source_reference=None, deposit_transaction_deposit_type=None, deposit_transaction_description=None, deposit_transaction_amount=None, deposit_transaction_date=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction - a model defined in OpenAPI

        :param deposit_transaction_source_reference: The deposit_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_source_reference: str
        :param deposit_transaction_deposit_type: The deposit_transaction_deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_deposit_type: str
        :param deposit_transaction_description: The deposit_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_description: str
        :param deposit_transaction_amount: The deposit_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_amount: str
        :param deposit_transaction_date: The deposit_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_date: str
        """
        self.openapi_types = {
            'deposit_transaction_source_reference': str,
            'deposit_transaction_deposit_type': str,
            'deposit_transaction_description': str,
            'deposit_transaction_amount': str,
            'deposit_transaction_date': str
        }

        self.attribute_map = {
            'deposit_transaction_source_reference': 'depositTransactionSourceReference',
            'deposit_transaction_deposit_type': 'depositTransactionDepositType',
            'deposit_transaction_description': 'depositTransactionDescription',
            'deposit_transaction_amount': 'depositTransactionAmount',
            'deposit_transaction_date': 'depositTransactionDate'
        }

        self._deposit_transaction_source_reference = deposit_transaction_source_reference
        self._deposit_transaction_deposit_type = deposit_transaction_deposit_type
        self._deposit_transaction_description = deposit_transaction_description
        self._deposit_transaction_amount = deposit_transaction_amount
        self._deposit_transaction_date = deposit_transaction_date

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__depositsandwithdrawals__bq_reference_id__execution_depositsAndWithdrawalsInstanceRecord_depositTransaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposit_transaction_source_reference(self):
        """Gets the deposit_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Identifies the source of the deposit   # noqa: E501

        :return: The deposit_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_source_reference

    @deposit_transaction_source_reference.setter
    def deposit_transaction_source_reference(self, deposit_transaction_source_reference):
        """Sets the deposit_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Identifies the source of the deposit   # noqa: E501

        :param deposit_transaction_source_reference: The deposit_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_source_reference: str
        """

        self._deposit_transaction_source_reference = deposit_transaction_source_reference

    @property
    def deposit_transaction_deposit_type(self):
        """Gets the deposit_transaction_deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of deposit made with the transaction   # noqa: E501

        :return: The deposit_transaction_deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_deposit_type

    @deposit_transaction_deposit_type.setter
    def deposit_transaction_deposit_type(self, deposit_transaction_deposit_type):
        """Sets the deposit_transaction_deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of deposit made with the transaction   # noqa: E501

        :param deposit_transaction_deposit_type: The deposit_transaction_deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_deposit_type: str
        """

        self._deposit_transaction_deposit_type = deposit_transaction_deposit_type

    @property
    def deposit_transaction_description(self):
        """Gets the deposit_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Any necessary details describing the purpose or reference properties of the deposit   # noqa: E501

        :return: The deposit_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_description

    @deposit_transaction_description.setter
    def deposit_transaction_description(self, deposit_transaction_description):
        """Sets the deposit_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Any necessary details describing the purpose or reference properties of the deposit   # noqa: E501

        :param deposit_transaction_description: The deposit_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_description: str
        """

        self._deposit_transaction_description = deposit_transaction_description

    @property
    def deposit_transaction_amount(self):
        """Gets the deposit_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The deposited amount   # noqa: E501

        :return: The deposit_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_amount

    @deposit_transaction_amount.setter
    def deposit_transaction_amount(self, deposit_transaction_amount):
        """Sets the deposit_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The deposited amount   # noqa: E501

        :param deposit_transaction_amount: The deposit_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_amount: str
        """

        self._deposit_transaction_amount = deposit_transaction_amount

    @property
    def deposit_transaction_date(self):
        """Gets the deposit_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the deposit was initiated   # noqa: E501

        :return: The deposit_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_date

    @deposit_transaction_date.setter
    def deposit_transaction_date(self, deposit_transaction_date):
        """Sets the deposit_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the deposit was initiated   # noqa: E501

        :param deposit_transaction_date: The deposit_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_date: str
        """

        self._deposit_transaction_date = deposit_transaction_date
