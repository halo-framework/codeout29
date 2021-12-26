# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_sweep_target_account=None, account_sweep_amount=None, account_sweep_execution_date=None):  # noqa: E501
        """BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord - a model defined in OpenAPI

        :param account_sweep_target_account: The account_sweep_target_account of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.  # noqa: E501
        :type account_sweep_target_account: str
        :param account_sweep_amount: The account_sweep_amount of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.  # noqa: E501
        :type account_sweep_amount: str
        :param account_sweep_execution_date: The account_sweep_execution_date of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.  # noqa: E501
        :type account_sweep_execution_date: str
        """
        self.openapi_types = {
            'account_sweep_target_account': str,
            'account_sweep_amount': str,
            'account_sweep_execution_date': str
        }

        self.attribute_map = {
            'account_sweep_target_account': 'accountSweepTargetAccount',
            'account_sweep_amount': 'accountSweepAmount',
            'account_sweep_execution_date': 'accountSweepExecutionDate'
        }

        self._account_sweep_target_account = account_sweep_target_account
        self._account_sweep_amount = account_sweep_amount
        self._account_sweep_execution_date = account_sweep_execution_date

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountSweepUpdateInputModel_accountSweepInstanceRecord_sweepApplicationRecord of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.  # noqa: E501
        :rtype: BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_sweep_target_account(self):
        """Gets the account_sweep_target_account of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The facility that the sweep is made to/from   # noqa: E501

        :return: The account_sweep_target_account of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :rtype: str
        """
        return self._account_sweep_target_account

    @account_sweep_target_account.setter
    def account_sweep_target_account(self, account_sweep_target_account):
        """Sets the account_sweep_target_account of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The facility that the sweep is made to/from   # noqa: E501

        :param account_sweep_target_account: The account_sweep_target_account of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :type account_sweep_target_account: str
        """

        self._account_sweep_target_account = account_sweep_target_account

    @property
    def account_sweep_amount(self):
        """Gets the account_sweep_amount of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The amount transferred to or from the account   # noqa: E501

        :return: The account_sweep_amount of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :rtype: str
        """
        return self._account_sweep_amount

    @account_sweep_amount.setter
    def account_sweep_amount(self, account_sweep_amount):
        """Sets the account_sweep_amount of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The amount transferred to or from the account   # noqa: E501

        :param account_sweep_amount: The account_sweep_amount of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :type account_sweep_amount: str
        """

        self._account_sweep_amount = account_sweep_amount

    @property
    def account_sweep_execution_date(self):
        """Gets the account_sweep_execution_date of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the sweep is initiated   # noqa: E501

        :return: The account_sweep_execution_date of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :rtype: str
        """
        return self._account_sweep_execution_date

    @account_sweep_execution_date.setter
    def account_sweep_execution_date(self, account_sweep_execution_date):
        """Sets the account_sweep_execution_date of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date and time the sweep is initiated   # noqa: E501

        :param account_sweep_execution_date: The account_sweep_execution_date of this BQAccountSweepUpdateInputModelAccountSweepInstanceRecordSweepApplicationRecord.
        :type account_sweep_execution_date: str
        """

        self._account_sweep_execution_date = account_sweep_execution_date