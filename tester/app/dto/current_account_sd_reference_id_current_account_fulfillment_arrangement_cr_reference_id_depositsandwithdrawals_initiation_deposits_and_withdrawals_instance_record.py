# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposit_type=None, withdrawal_type=None, account_limit_breach_response=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord - a model defined in OpenAPI

        :param deposit_type: The deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type deposit_type: str
        :param withdrawal_type: The withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type withdrawal_type: str
        :param account_limit_breach_response: The account_limit_breach_response of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :type account_limit_breach_response: str
        """
        self.openapi_types = {
            'deposit_type': str,
            'withdrawal_type': str,
            'account_limit_breach_response': str
        }

        self.attribute_map = {
            'deposit_type': 'depositType',
            'withdrawal_type': 'withdrawalType',
            'account_limit_breach_response': 'accountLimitBreachResponse'
        }

        self._deposit_type = deposit_type
        self._withdrawal_type = withdrawal_type
        self._account_limit_breach_response = account_limit_breach_response

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__depositsandwithdrawals_initiation_depositsAndWithdrawalsInstanceRecord of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposit_type(self):
        """Gets the deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5_m2sTGEeChad0JzLk7QA_-2008690148/elements/_E6IwwMTGEeChad0JzLk7QA_1495654231  bian-reference: DepositServicet.DepositType  general-info: The type of deposit transaction that can be applied to the account (e.g. customer deposit, internal credit)   # noqa: E501

        :return: The deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._deposit_type

    @deposit_type.setter
    def deposit_type(self, deposit_type):
        """Sets the deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5_m2sTGEeChad0JzLk7QA_-2008690148/elements/_E6IwwMTGEeChad0JzLk7QA_1495654231  bian-reference: DepositServicet.DepositType  general-info: The type of deposit transaction that can be applied to the account (e.g. customer deposit, internal credit)   # noqa: E501

        :param deposit_type: The deposit_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :type deposit_type: str
        """

        self._deposit_type = deposit_type

    @property
    def withdrawal_type(self):
        """Gets the withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal transaction that can be applied to the account (e.g. customer withdrawal, internal service charge, disbursement)   # noqa: E501

        :return: The withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._withdrawal_type

    @withdrawal_type.setter
    def withdrawal_type(self, withdrawal_type):
        """Sets the withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of withdrawal transaction that can be applied to the account (e.g. customer withdrawal, internal service charge, disbursement)   # noqa: E501

        :param withdrawal_type: The withdrawal_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :type withdrawal_type: str
        """

        self._withdrawal_type = withdrawal_type

    @property
    def account_limit_breach_response(self):
        """Gets the account_limit_breach_response of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The handling options if a withdrawal results in a breach of an account limit   # noqa: E501

        :return: The account_limit_breach_response of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :rtype: str
        """
        return self._account_limit_breach_response

    @account_limit_breach_response.setter
    def account_limit_breach_response(self, account_limit_breach_response):
        """Sets the account_limit_breach_response of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The handling options if a withdrawal results in a breach of an account limit   # noqa: E501

        :param account_limit_breach_response: The account_limit_breach_response of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdDepositsandwithdrawalsInitiationDepositsAndWithdrawalsInstanceRecord.
        :type account_limit_breach_response: str
        """

        self._account_limit_breach_response = account_limit_breach_response
