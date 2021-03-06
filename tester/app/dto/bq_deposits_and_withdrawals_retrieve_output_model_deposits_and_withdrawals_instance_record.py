# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record_deposit_transaction import InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record_withdrawal_transaction import InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
from tester import util

from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record_deposit_transaction import InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction  # noqa: E501
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record_withdrawal_transaction import InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction  # noqa: E501



class BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposit_type=None, withdrawal_type=None, account_limit_breach_response=None, deposit_transaction=None, withdrawal_transaction=None):  # noqa: E501
        """BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord - a model defined in OpenAPI

        :param deposit_type: The deposit_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type deposit_type: str
        :param withdrawal_type: The withdrawal_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type withdrawal_type: str
        :param account_limit_breach_response: The account_limit_breach_response of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type account_limit_breach_response: str
        :param deposit_transaction: The deposit_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type deposit_transaction: InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction
        :param withdrawal_transaction: The withdrawal_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type withdrawal_transaction: InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
        """
        self.openapi_types = {
            'deposit_type': str,
            'withdrawal_type': str,
            'account_limit_breach_response': str,
            'deposit_transaction': InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction,
            'withdrawal_transaction': InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
        }

        self.attribute_map = {
            'deposit_type': 'depositType',
            'withdrawal_type': 'withdrawalType',
            'account_limit_breach_response': 'accountLimitBreachResponse',
            'deposit_transaction': 'depositTransaction',
            'withdrawal_transaction': 'withdrawalTransaction'
        }

        self._deposit_type = deposit_type
        self._withdrawal_type = withdrawal_type
        self._account_limit_breach_response = account_limit_breach_response
        self._deposit_transaction = deposit_transaction
        self._withdrawal_transaction = withdrawal_transaction

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsRetrieveOutputModel_depositsAndWithdrawalsInstanceRecord of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposit_type(self):
        """Gets the deposit_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5_m2sTGEeChad0JzLk7QA_-2008690148/elements/_E6IwwMTGEeChad0JzLk7QA_1495654231  bian-reference: DepositServicet.DepositType  general-info: The type of deposit transaction that can be applied to the account (e.g. customer deposit, internal credit)   # noqa: E501

        :return: The deposit_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._deposit_type

    @deposit_type.setter
    def deposit_type(self, deposit_type):
        """Sets the deposit_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5_m2sTGEeChad0JzLk7QA_-2008690148/elements/_E6IwwMTGEeChad0JzLk7QA_1495654231  bian-reference: DepositServicet.DepositType  general-info: The type of deposit transaction that can be applied to the account (e.g. customer deposit, internal credit)   # noqa: E501

        :param deposit_type: The deposit_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :type deposit_type: str
        """

        self._deposit_type = deposit_type

    @property
    def withdrawal_type(self):
        """Gets the withdrawal_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal transaction that can be applied to the account (e.g. customer withdrawal, internal service charge, disbursement)   # noqa: E501

        :return: The withdrawal_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._withdrawal_type

    @withdrawal_type.setter
    def withdrawal_type(self, withdrawal_type):
        """Sets the withdrawal_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal transaction that can be applied to the account (e.g. customer withdrawal, internal service charge, disbursement)   # noqa: E501

        :param withdrawal_type: The withdrawal_type of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :type withdrawal_type: str
        """

        self._withdrawal_type = withdrawal_type

    @property
    def account_limit_breach_response(self):
        """Gets the account_limit_breach_response of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The handling options if a withdrawal results in a breach of an account limit   # noqa: E501

        :return: The account_limit_breach_response of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._account_limit_breach_response

    @account_limit_breach_response.setter
    def account_limit_breach_response(self, account_limit_breach_response):
        """Sets the account_limit_breach_response of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The handling options if a withdrawal results in a breach of an account limit   # noqa: E501

        :param account_limit_breach_response: The account_limit_breach_response of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :type account_limit_breach_response: str
        """

        self._account_limit_breach_response = account_limit_breach_response

    @property
    def deposit_transaction(self):
        """Gets the deposit_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.


        :return: The deposit_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction
        """
        return self._deposit_transaction

    @deposit_transaction.setter
    def deposit_transaction(self, deposit_transaction):
        """Sets the deposit_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.


        :param deposit_transaction: The deposit_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :type deposit_transaction: InlineResponse20017DepositsAndWithdrawalsInstanceRecordDepositTransaction
        """

        self._deposit_transaction = deposit_transaction

    @property
    def withdrawal_transaction(self):
        """Gets the withdrawal_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.


        :return: The withdrawal_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
        """
        return self._withdrawal_transaction

    @withdrawal_transaction.setter
    def withdrawal_transaction(self, withdrawal_transaction):
        """Sets the withdrawal_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.


        :param withdrawal_transaction: The withdrawal_transaction of this BQDepositsAndWithdrawalsRetrieveOutputModelDepositsAndWithdrawalsInstanceRecord.
        :type withdrawal_transaction: InlineResponse20017DepositsAndWithdrawalsInstanceRecordWithdrawalTransaction
        """

        self._withdrawal_transaction = withdrawal_transaction
