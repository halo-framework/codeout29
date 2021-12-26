# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposit_transaction_date=None):  # noqa: E501
        """BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction - a model defined in OpenAPI

        :param deposit_transaction_date: The deposit_transaction_date of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :type deposit_transaction_date: str
        """
        self.openapi_types = {
            'deposit_transaction_date': str
        }

        self.attribute_map = {
            'deposit_transaction_date': 'depositTransactionDate'
        }

        self._deposit_transaction_date = deposit_transaction_date

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsExecuteOutputModel_depositsAndWithdrawalsInstanceRecord_depositTransaction of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposit_transaction_date(self):
        """Gets the deposit_transaction_date of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the deposit was initiated   # noqa: E501

        :return: The deposit_transaction_date of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :rtype: str
        """
        return self._deposit_transaction_date

    @deposit_transaction_date.setter
    def deposit_transaction_date(self, deposit_transaction_date):
        """Sets the deposit_transaction_date of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the deposit was initiated   # noqa: E501

        :param deposit_transaction_date: The deposit_transaction_date of this BQDepositsAndWithdrawalsExecuteOutputModelDepositsAndWithdrawalsInstanceRecordDepositTransaction.
        :type deposit_transaction_date: str
        """

        self._deposit_transaction_date = deposit_transaction_date