# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
from tester.app.dto.inline_response2011_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts  # noqa: E501
from tester.app.dto.inline_response2011_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits  # noqa: E501



class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, product_instance_reference=None, current_account_number=None, account_type=None, account_currency=None, tax_reference=None, restriction_option_setting=None, linked_accounts=None, position_limits=None, date_type=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord - a model defined in OpenAPI

        :param product_instance_reference: The product_instance_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type product_instance_reference: str
        :param current_account_number: The current_account_number of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type current_account_number: str
        :param account_type: The account_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type account_type: str
        :param account_currency: The account_currency of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type account_currency: str
        :param tax_reference: The tax_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type tax_reference: str
        :param restriction_option_setting: The restriction_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type restriction_option_setting: str
        :param linked_accounts: The linked_accounts of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        :param position_limits: The position_limits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type position_limits: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        :param date_type: The date_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        self.openapi_types = {
            'product_instance_reference': str,
            'current_account_number': str,
            'account_type': str,
            'account_currency': str,
            'tax_reference': str,
            'restriction_option_setting': str,
            'linked_accounts': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts,
            'position_limits': InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits,
            'date_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        }

        self.attribute_map = {
            'product_instance_reference': 'productInstanceReference',
            'current_account_number': 'currentAccountNumber',
            'account_type': 'accountType',
            'account_currency': 'accountCurrency',
            'tax_reference': 'taxReference',
            'restriction_option_setting': 'restrictionOptionSetting',
            'linked_accounts': 'linkedAccounts',
            'position_limits': 'positionLimits',
            'date_type': 'dateType'
        }

        self._product_instance_reference = product_instance_reference
        self._current_account_number = current_account_number
        self._account_type = account_type
        self._account_currency = account_currency
        self._tax_reference = tax_reference
        self._restriction_option_setting = restriction_option_setting
        self._linked_accounts = linked_accounts
        self._position_limits = position_limits
        self._date_type = date_type

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__servicefees_initiation_currentAccountFulfillmentArrangementInstanceRecord of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product_instance_reference(self):
        """Gets the product_instance_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the current account product instance   # noqa: E501

        :return: The product_instance_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._product_instance_reference

    @product_instance_reference.setter
    def product_instance_reference(self, product_instance_reference):
        """Sets the product_instance_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the current account product instance   # noqa: E501

        :param product_instance_reference: The product_instance_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type product_instance_reference: str
        """

        self._product_instance_reference = product_instance_reference

    @property
    def current_account_number(self):
        """Gets the current_account_number of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_E1rHhcTGEeChad0JzLk7QA_-755813725  bian-reference: CurrentAccount (as Account).AccountIdentification  general-info: The associated account number in any suitable format (e.g. IBAN)   # noqa: E501

        :return: The current_account_number of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._current_account_number

    @current_account_number.setter
    def current_account_number(self, current_account_number):
        """Sets the current_account_number of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_E1rHhcTGEeChad0JzLk7QA_-755813725  bian-reference: CurrentAccount (as Account).AccountIdentification  general-info: The associated account number in any suitable format (e.g. IBAN)   # noqa: E501

        :param current_account_number: The current_account_number of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type current_account_number: str
        """

        self._current_account_number = current_account_number

    @property
    def account_type(self):
        """Gets the account_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_7CvjsPj5EeG2rK1g72xi7Q_-843966450  bian-reference: CurrentAccount (as Account).AccountType  general-info: The type of current account (e.g. checking, student, small business)   # noqa: E501

        :return: The account_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_7CvjsPj5EeG2rK1g72xi7Q_-843966450  bian-reference: CurrentAccount (as Account).AccountType  general-info: The type of current account (e.g. checking, student, small business)   # noqa: E501

        :param account_type: The account_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type account_type: str
        """

        self._account_type = account_type

    @property
    def account_currency(self):
        """Gets the account_currency of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :return: The account_currency of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._account_currency

    @account_currency.setter
    def account_currency(self, account_currency):
        """Sets the account_currency of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :param account_currency: The account_currency of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type account_currency: str
        """

        self._account_currency = account_currency

    @property
    def tax_reference(self):
        """Gets the tax_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E4gZEcTGEeChad0JzLk7QA_2010102987/elements/__-5BiGIiEeGD28DQaMef-g  bian-reference: CurrentAccountAgreement (as Agreement). RuleSetAsRegulation  general-info: Reference identifier linking the account to appropriate tax handling   # noqa: E501

        :return: The tax_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._tax_reference

    @tax_reference.setter
    def tax_reference(self, tax_reference):
        """Sets the tax_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E4gZEcTGEeChad0JzLk7QA_2010102987/elements/__-5BiGIiEeGD28DQaMef-g  bian-reference: CurrentAccountAgreement (as Agreement). RuleSetAsRegulation  general-info: Reference identifier linking the account to appropriate tax handling   # noqa: E501

        :param tax_reference: The tax_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type tax_reference: str
        """

        self._tax_reference = tax_reference

    @property
    def restriction_option_setting(self):
        """Gets the restriction_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :return: The restriction_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._restriction_option_setting

    @restriction_option_setting.setter
    def restriction_option_setting(self, restriction_option_setting):
        """Sets the restriction_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :param restriction_option_setting: The restriction_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type restriction_option_setting: str
        """

        self._restriction_option_setting = restriction_option_setting

    @property
    def linked_accounts(self):
        """Gets the linked_accounts of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The linked_accounts of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """
        return self._linked_accounts

    @linked_accounts.setter
    def linked_accounts(self, linked_accounts):
        """Sets the linked_accounts of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :param linked_accounts: The linked_accounts of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """

        self._linked_accounts = linked_accounts

    @property
    def position_limits(self):
        """Gets the position_limits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The position_limits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return self._position_limits

    @position_limits.setter
    def position_limits(self, position_limits):
        """Sets the position_limits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :param position_limits: The position_limits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type position_limits: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """

        self._position_limits = position_limits

    @property
    def date_type(self):
        """Gets the date_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The date_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.


        :param date_type: The date_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationCurrentAccountFulfillmentArrangementInstanceRecord.
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """

        self._date_type = date_type