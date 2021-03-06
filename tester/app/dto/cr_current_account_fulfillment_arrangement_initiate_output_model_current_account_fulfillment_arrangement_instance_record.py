# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
from tester.app.dto.inline_response2011_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType  # noqa: E501
from tester.app.dto.inline_response2011_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits  # noqa: E501



class CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, product_instance_reference=None, current_account_number=None, account_currency=None, entitlement_option_definition=None, entitlement_option_setting=None, restriction_option_definition=None, restriction_option_setting=None, position_limits=None, date_type=None):  # noqa: E501
        """CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord - a model defined in OpenAPI

        :param product_instance_reference: The product_instance_reference of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type product_instance_reference: str
        :param current_account_number: The current_account_number of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type current_account_number: str
        :param account_currency: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type account_currency: str
        :param entitlement_option_definition: The entitlement_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type entitlement_option_definition: str
        :param entitlement_option_setting: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type entitlement_option_setting: str
        :param restriction_option_definition: The restriction_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type restriction_option_definition: str
        :param restriction_option_setting: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type restriction_option_setting: str
        :param position_limits: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type position_limits: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        :param date_type: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        self.openapi_types = {
            'product_instance_reference': str,
            'current_account_number': str,
            'account_currency': str,
            'entitlement_option_definition': str,
            'entitlement_option_setting': str,
            'restriction_option_definition': str,
            'restriction_option_setting': str,
            'position_limits': InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits,
            'date_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        }

        self.attribute_map = {
            'product_instance_reference': 'productInstanceReference',
            'current_account_number': 'currentAccountNumber',
            'account_currency': 'accountCurrency',
            'entitlement_option_definition': 'entitlementOptionDefinition',
            'entitlement_option_setting': 'entitlementOptionSetting',
            'restriction_option_definition': 'restrictionOptionDefinition',
            'restriction_option_setting': 'restrictionOptionSetting',
            'position_limits': 'positionLimits',
            'date_type': 'dateType'
        }

        self._product_instance_reference = product_instance_reference
        self._current_account_number = current_account_number
        self._account_currency = account_currency
        self._entitlement_option_definition = entitlement_option_definition
        self._entitlement_option_setting = entitlement_option_setting
        self._restriction_option_definition = restriction_option_definition
        self._restriction_option_setting = restriction_option_setting
        self._position_limits = position_limits
        self._date_type = date_type

    @classmethod
    def from_dict(cls, dikt) -> 'CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CRCurrentAccountFulfillmentArrangementInitiateOutputModel_currentAccountFulfillmentArrangementInstanceRecord of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :rtype: CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product_instance_reference(self):
        """Gets the product_instance_reference of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the current account product instance   # noqa: E501

        :return: The product_instance_reference of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._product_instance_reference

    @product_instance_reference.setter
    def product_instance_reference(self, product_instance_reference):
        """Sets the product_instance_reference of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the current account product instance   # noqa: E501

        :param product_instance_reference: The product_instance_reference of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type product_instance_reference: str
        """

        self._product_instance_reference = product_instance_reference

    @property
    def current_account_number(self):
        """Gets the current_account_number of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_E1rHhcTGEeChad0JzLk7QA_-755813725  bian-reference: CurrentAccount (as Account).AccountIdentification  general-info: The associated account number in any suitable format (e.g. IBAN)   # noqa: E501

        :return: The current_account_number of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._current_account_number

    @current_account_number.setter
    def current_account_number(self, current_account_number):
        """Sets the current_account_number of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_E1rHhcTGEeChad0JzLk7QA_-755813725  bian-reference: CurrentAccount (as Account).AccountIdentification  general-info: The associated account number in any suitable format (e.g. IBAN)   # noqa: E501

        :param current_account_number: The current_account_number of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type current_account_number: str
        """

        self._current_account_number = current_account_number

    @property
    def account_currency(self):
        """Gets the account_currency of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :return: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._account_currency

    @account_currency.setter
    def account_currency(self, account_currency):
        """Sets the account_currency of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E1rHgsTGEeChad0JzLk7QA_-1068889728/elements/_-69C4IDWEeKn8fN1QdMTXQ_-145666344  bian-reference: CurrentAccount (as Account).AccountBaseCurrency  general-info: The primary account currency   # noqa: E501

        :param account_currency: The account_currency of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type account_currency: str
        """

        self._account_currency = account_currency

    @property
    def entitlement_option_definition(self):
        """Gets the entitlement_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable entitlement option   # noqa: E501

        :return: The entitlement_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._entitlement_option_definition

    @entitlement_option_definition.setter
    def entitlement_option_definition(self, entitlement_option_definition):
        """Sets the entitlement_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable entitlement option   # noqa: E501

        :param entitlement_option_definition: The entitlement_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type entitlement_option_definition: str
        """

        self._entitlement_option_definition = entitlement_option_definition

    @property
    def entitlement_option_setting(self):
        """Gets the entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the entitlement option   # noqa: E501

        :return: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._entitlement_option_setting

    @entitlement_option_setting.setter
    def entitlement_option_setting(self, entitlement_option_setting):
        """Sets the entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the entitlement option   # noqa: E501

        :param entitlement_option_setting: The entitlement_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type entitlement_option_setting: str
        """

        self._entitlement_option_setting = entitlement_option_setting

    @property
    def restriction_option_definition(self):
        """Gets the restriction_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable restriction option   # noqa: E501

        :return: The restriction_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._restriction_option_definition

    @restriction_option_definition.setter
    def restriction_option_definition(self, restriction_option_definition):
        """Sets the restriction_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable restriction option   # noqa: E501

        :param restriction_option_definition: The restriction_option_definition of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type restriction_option_definition: str
        """

        self._restriction_option_definition = restriction_option_definition

    @property
    def restriction_option_setting(self):
        """Gets the restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :return: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._restriction_option_setting

    @restriction_option_setting.setter
    def restriction_option_setting(self, restriction_option_setting):
        """Sets the restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The setting for the restriction option   # noqa: E501

        :param restriction_option_setting: The restriction_option_setting of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type restriction_option_setting: str
        """

        self._restriction_option_setting = restriction_option_setting

    @property
    def position_limits(self):
        """Gets the position_limits of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return self._position_limits

    @position_limits.setter
    def position_limits(self, position_limits):
        """Sets the position_limits of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param position_limits: The position_limits of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type position_limits: InlineResponse2011CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """

        self._position_limits = position_limits

    @property
    def date_type(self):
        """Gets the date_type of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param date_type: The date_type of this CRCurrentAccountFulfillmentArrangementInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """

        self._date_type = date_type
