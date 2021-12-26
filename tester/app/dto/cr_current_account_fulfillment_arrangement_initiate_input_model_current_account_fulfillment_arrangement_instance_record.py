# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_associations import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_position_limits import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_associations import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_position_limits import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits  # noqa: E501



class CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, customer_reference=None, bank_branch_location_reference=None, account_type=None, account_currency=None, tax_reference=None, entitlement_option_setting=None, restriction_option_setting=None, associations=None, linked_accounts=None, position_limits=None, date_type=None):  # noqa: E501
        """CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord - a model defined in OpenAPI

        :param customer_reference: The customer_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type customer_reference: str
        :param bank_branch_location_reference: The bank_branch_location_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type bank_branch_location_reference: str
        :param account_type: The account_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type account_type: str
        :param account_currency: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type account_currency: str
        :param tax_reference: The tax_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type tax_reference: str
        :param entitlement_option_setting: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type entitlement_option_setting: str
        :param restriction_option_setting: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type restriction_option_setting: str
        :param associations: The associations of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type associations: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations
        :param linked_accounts: The linked_accounts of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        :param position_limits: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type position_limits: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        :param date_type: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        self.openapi_types = {
            'customer_reference': str,
            'bank_branch_location_reference': str,
            'account_type': str,
            'account_currency': str,
            'tax_reference': str,
            'entitlement_option_setting': str,
            'restriction_option_setting': str,
            'associations': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations,
            'linked_accounts': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts,
            'position_limits': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits,
            'date_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        }

        self.attribute_map = {
            'customer_reference': 'customerReference',
            'bank_branch_location_reference': 'bankBranchLocationReference',
            'account_type': 'accountType',
            'account_currency': 'accountCurrency',
            'tax_reference': 'taxReference',
            'entitlement_option_setting': 'entitlementOptionSetting',
            'restriction_option_setting': 'restrictionOptionSetting',
            'associations': 'associations',
            'linked_accounts': 'linkedAccounts',
            'position_limits': 'positionLimits',
            'date_type': 'dateType'
        }

        self._customer_reference = customer_reference
        self._bank_branch_location_reference = bank_branch_location_reference
        self._account_type = account_type
        self._account_currency = account_currency
        self._tax_reference = tax_reference
        self._entitlement_option_setting = entitlement_option_setting
        self._restriction_option_setting = restriction_option_setting
        self._associations = associations
        self._linked_accounts = linked_accounts
        self._position_limits = position_limits
        self._date_type = date_type

    @classmethod
    def from_dict(cls, dikt) -> 'CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CRCurrentAccountFulfillmentArrangementInitiateInputModel_currentAccountFulfillmentArrangementInstanceRecord of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :rtype: CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_reference(self):
        """Gets the customer_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EysE9cTGEeChad0JzLk7QA_-200588046  bian-reference: CurrentAccount (as Account).AccountInvolvement (as AccountOwner)  general-info: Reference to the account primary party/owner   # noqa: E501

        :return: The customer_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._customer_reference

    @customer_reference.setter
    def customer_reference(self, customer_reference):
        """Sets the customer_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EysE9cTGEeChad0JzLk7QA_-200588046  bian-reference: CurrentAccount (as Account).AccountInvolvement (as AccountOwner)  general-info: Reference to the account primary party/owner   # noqa: E501

        :param customer_reference: The customer_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type customer_reference: str
        """

        self._customer_reference = customer_reference

    @property
    def bank_branch_location_reference(self):
        """Gets the bank_branch_location_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FNqJt8TGEeChad0JzLk7QA_-1317971633/elements/_z2I6YGx5EeKmZJ0Ago--9g_239738909  bian-reference: CurrentAccount (as Account).AccountInvolvement (as AccountServicer). PartyRole.Party.Location  general-info: Bank branch associated with the account for booking purposes   # noqa: E501

        :return: The bank_branch_location_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._bank_branch_location_reference

    @bank_branch_location_reference.setter
    def bank_branch_location_reference(self, bank_branch_location_reference):
        """Sets the bank_branch_location_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FNqJt8TGEeChad0JzLk7QA_-1317971633/elements/_z2I6YGx5EeKmZJ0Ago--9g_239738909  bian-reference: CurrentAccount (as Account).AccountInvolvement (as AccountServicer). PartyRole.Party.Location  general-info: Bank branch associated with the account for booking purposes   # noqa: E501

        :param bank_branch_location_reference: The bank_branch_location_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type bank_branch_location_reference: str
        """

        self._bank_branch_location_reference = bank_branch_location_reference

    @property
    def account_type(self):
        """Gets the account_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_7CvjsPj5EeG2rK1g72xi7Q_-843966450  bian-reference: CurrentAccount (as Account).AccountType  general-info: The type of current account (e.g. checking, student, small business)   # noqa: E501

        :return: The account_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_7CvjsPj5EeG2rK1g72xi7Q_-843966450  bian-reference: CurrentAccount (as Account).AccountType  general-info: The type of current account (e.g. checking, student, small business)   # noqa: E501

        :param account_type: The account_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type account_type: str
        """

        self._account_type = account_type

    @property
    def account_currency(self):
        """Gets the account_currency of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :return: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._account_currency

    @account_currency.setter
    def account_currency(self, account_currency):
        """Sets the account_currency of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :param account_currency: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type account_currency: str
        """

        self._account_currency = account_currency

    @property
    def tax_reference(self):
        """Gets the tax_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E4gZEcTGEeChad0JzLk7QA_2010102987/elements/__-5BiGIiEeGD28DQaMef-g  bian-reference: CurrentAccountAgreement (as Agreement). RuleSetAsRegulation  general-info: Reference identifier linking the account to appropriate tax handling   # noqa: E501

        :return: The tax_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._tax_reference

    @tax_reference.setter
    def tax_reference(self, tax_reference):
        """Sets the tax_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E4gZEcTGEeChad0JzLk7QA_2010102987/elements/__-5BiGIiEeGD28DQaMef-g  bian-reference: CurrentAccountAgreement (as Agreement). RuleSetAsRegulation  general-info: Reference identifier linking the account to appropriate tax handling   # noqa: E501

        :param tax_reference: The tax_reference of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type tax_reference: str
        """

        self._tax_reference = tax_reference

    @property
    def entitlement_option_setting(self):
        """Gets the entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the entitlement option   # noqa: E501

        :return: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._entitlement_option_setting

    @entitlement_option_setting.setter
    def entitlement_option_setting(self, entitlement_option_setting):
        """Sets the entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the entitlement option   # noqa: E501

        :param entitlement_option_setting: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type entitlement_option_setting: str
        """

        self._entitlement_option_setting = entitlement_option_setting

    @property
    def restriction_option_setting(self):
        """Gets the restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :return: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._restriction_option_setting

    @restriction_option_setting.setter
    def restriction_option_setting(self, restriction_option_setting):
        """Sets the restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :param restriction_option_setting: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type restriction_option_setting: str
        """

        self._restriction_option_setting = restriction_option_setting

    @property
    def associations(self):
        """Gets the associations of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The associations of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param associations: The associations of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type associations: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordAssociations
        """

        self._associations = associations

    @property
    def linked_accounts(self):
        """Gets the linked_accounts of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The linked_accounts of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """
        return self._linked_accounts

    @linked_accounts.setter
    def linked_accounts(self, linked_accounts):
        """Sets the linked_accounts of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param linked_accounts: The linked_accounts of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """

        self._linked_accounts = linked_accounts

    @property
    def position_limits(self):
        """Gets the position_limits of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return self._position_limits

    @position_limits.setter
    def position_limits(self, position_limits):
        """Sets the position_limits of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param position_limits: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type position_limits: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """

        self._position_limits = position_limits

    @property
    def date_type(self):
        """Gets the date_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param date_type: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """

        self._date_type = date_type