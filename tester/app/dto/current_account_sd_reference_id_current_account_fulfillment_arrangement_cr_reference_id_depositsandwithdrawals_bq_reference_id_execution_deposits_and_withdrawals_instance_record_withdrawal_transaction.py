# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, withdrawal_transaction_source_reference=None, withdrawal_transaction_withdrawal_type=None, withdrawal_transaction_description=None, withdrawal_transaction_amount=None, withdrawal_transaction_date=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction - a model defined in OpenAPI

        :param withdrawal_transaction_source_reference: The withdrawal_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :type withdrawal_transaction_source_reference: str
        :param withdrawal_transaction_withdrawal_type: The withdrawal_transaction_withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :type withdrawal_transaction_withdrawal_type: str
        :param withdrawal_transaction_description: The withdrawal_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :type withdrawal_transaction_description: str
        :param withdrawal_transaction_amount: The withdrawal_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :type withdrawal_transaction_amount: str
        :param withdrawal_transaction_date: The withdrawal_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :type withdrawal_transaction_date: str
        """
        self.openapi_types = {
            'withdrawal_transaction_source_reference': str,
            'withdrawal_transaction_withdrawal_type': str,
            'withdrawal_transaction_description': str,
            'withdrawal_transaction_amount': str,
            'withdrawal_transaction_date': str
        }

        self.attribute_map = {
            'withdrawal_transaction_source_reference': 'withdrawalTransactionSourceReference',
            'withdrawal_transaction_withdrawal_type': 'withdrawalTransactionWithdrawalType',
            'withdrawal_transaction_description': 'withdrawalTransactionDescription',
            'withdrawal_transaction_amount': 'withdrawalTransactionAmount',
            'withdrawal_transaction_date': 'withdrawalTransactionDate'
        }

        self._withdrawal_transaction_source_reference = withdrawal_transaction_source_reference
        self._withdrawal_transaction_withdrawal_type = withdrawal_transaction_withdrawal_type
        self._withdrawal_transaction_description = withdrawal_transaction_description
        self._withdrawal_transaction_amount = withdrawal_transaction_amount
        self._withdrawal_transaction_date = withdrawal_transaction_date

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__depositsandwithdrawals__bq_reference_id__execution_depositsAndWithdrawalsInstanceRecord_withdrawalTransaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def withdrawal_transaction_source_reference(self):
        """Gets the withdrawal_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Identifies the target for the withdrawal   # noqa: E501

        :return: The withdrawal_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :rtype: str
        """
        return self._withdrawal_transaction_source_reference

    @withdrawal_transaction_source_reference.setter
    def withdrawal_transaction_source_reference(self, withdrawal_transaction_source_reference):
        """Sets the withdrawal_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Identifies the target for the withdrawal   # noqa: E501

        :param withdrawal_transaction_source_reference: The withdrawal_transaction_source_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :type withdrawal_transaction_source_reference: str
        """

        self._withdrawal_transaction_source_reference = withdrawal_transaction_source_reference

    @property
    def withdrawal_transaction_withdrawal_type(self):
        """Gets the withdrawal_transaction_withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal made with the transaction   # noqa: E501

        :return: The withdrawal_transaction_withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :rtype: str
        """
        return self._withdrawal_transaction_withdrawal_type

    @withdrawal_transaction_withdrawal_type.setter
    def withdrawal_transaction_withdrawal_type(self, withdrawal_transaction_withdrawal_type):
        """Sets the withdrawal_transaction_withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal made with the transaction   # noqa: E501

        :param withdrawal_transaction_withdrawal_type: The withdrawal_transaction_withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :type withdrawal_transaction_withdrawal_type: str
        """

        self._withdrawal_transaction_withdrawal_type = withdrawal_transaction_withdrawal_type

    @property
    def withdrawal_transaction_description(self):
        """Gets the withdrawal_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Any necessary details describing the purpose or reference properties of the withdrawal   # noqa: E501

        :return: The withdrawal_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :rtype: str
        """
        return self._withdrawal_transaction_description

    @withdrawal_transaction_description.setter
    def withdrawal_transaction_description(self, withdrawal_transaction_description):
        """Sets the withdrawal_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Any necessary details describing the purpose or reference properties of the withdrawal   # noqa: E501

        :param withdrawal_transaction_description: The withdrawal_transaction_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :type withdrawal_transaction_description: str
        """

        self._withdrawal_transaction_description = withdrawal_transaction_description

    @property
    def withdrawal_transaction_amount(self):
        """Gets the withdrawal_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The withdrawn amount   # noqa: E501

        :return: The withdrawal_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :rtype: str
        """
        return self._withdrawal_transaction_amount

    @withdrawal_transaction_amount.setter
    def withdrawal_transaction_amount(self, withdrawal_transaction_amount):
        """Sets the withdrawal_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The withdrawn amount   # noqa: E501

        :param withdrawal_transaction_amount: The withdrawal_transaction_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :type withdrawal_transaction_amount: str
        """

        self._withdrawal_transaction_amount = withdrawal_transaction_amount

    @property
    def withdrawal_transaction_date(self):
        """Gets the withdrawal_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the withdrawal was initiated   # noqa: E501

        :return: The withdrawal_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :rtype: str
        """
        return self._withdrawal_transaction_date

    @withdrawal_transaction_date.setter
    def withdrawal_transaction_date(self, withdrawal_transaction_date):
        """Sets the withdrawal_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the withdrawal was initiated   # noqa: E501

        :param withdrawal_transaction_date: The withdrawal_transaction_date of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsBqReferenceIdExecutionDepositsAndWithdrawalsInstanceRecordWithdrawalTransaction.
        :type withdrawal_transaction_date: str
        """

        self._withdrawal_transaction_date = withdrawal_transaction_date
