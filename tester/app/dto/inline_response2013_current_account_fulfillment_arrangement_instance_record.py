# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
from tester.app.dto.inline_response2013_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_linked_accounts import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts  # noqa: E501
from tester.app.dto.inline_response2013_current_account_fulfillment_arrangement_instance_record_position_limits import InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits  # noqa: E501



class InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entitlement_option_definition=None, restriction_option_definition=None, linked_accounts=None, position_limits=None, date_type=None):  # noqa: E501
        """InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord - a model defined in OpenAPI

        :param entitlement_option_definition: The entitlement_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type entitlement_option_definition: str
        :param restriction_option_definition: The restriction_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type restriction_option_definition: str
        :param linked_accounts: The linked_accounts of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        :param position_limits: The position_limits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type position_limits: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        :param date_type: The date_type of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        self.openapi_types = {
            'entitlement_option_definition': str,
            'restriction_option_definition': str,
            'linked_accounts': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts,
            'position_limits': InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits,
            'date_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        }

        self.attribute_map = {
            'entitlement_option_definition': 'entitlementOptionDefinition',
            'restriction_option_definition': 'restrictionOptionDefinition',
            'linked_accounts': 'linkedAccounts',
            'position_limits': 'positionLimits',
            'date_type': 'dateType'
        }

        self._entitlement_option_definition = entitlement_option_definition
        self._restriction_option_definition = restriction_option_definition
        self._linked_accounts = linked_accounts
        self._position_limits = position_limits
        self._date_type = date_type

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_3_currentAccountFulfillmentArrangementInstanceRecord of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :rtype: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entitlement_option_definition(self):
        """Gets the entitlement_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable entitlement option   # noqa: E501

        :return: The entitlement_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._entitlement_option_definition

    @entitlement_option_definition.setter
    def entitlement_option_definition(self, entitlement_option_definition):
        """Sets the entitlement_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable entitlement option   # noqa: E501

        :param entitlement_option_definition: The entitlement_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :type entitlement_option_definition: str
        """

        self._entitlement_option_definition = entitlement_option_definition

    @property
    def restriction_option_definition(self):
        """Gets the restriction_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable restriction option   # noqa: E501

        :return: The restriction_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: str
        """
        return self._restriction_option_definition

    @restriction_option_definition.setter
    def restriction_option_definition(self, restriction_option_definition):
        """Sets the restriction_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The definition of an applicable restriction option   # noqa: E501

        :param restriction_option_definition: The restriction_option_definition of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :type restriction_option_definition: str
        """

        self._restriction_option_definition = restriction_option_definition

    @property
    def linked_accounts(self):
        """Gets the linked_accounts of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The linked_accounts of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """
        return self._linked_accounts

    @linked_accounts.setter
    def linked_accounts(self, linked_accounts):
        """Sets the linked_accounts of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :param linked_accounts: The linked_accounts of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :type linked_accounts: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordLinkedAccounts
        """

        self._linked_accounts = linked_accounts

    @property
    def position_limits(self):
        """Gets the position_limits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The position_limits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return self._position_limits

    @position_limits.setter
    def position_limits(self, position_limits):
        """Sets the position_limits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :param position_limits: The position_limits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :type position_limits: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """

        self._position_limits = position_limits

    @property
    def date_type(self):
        """Gets the date_type of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The date_type of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.


        :param date_type: The date_type of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecord.
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """

        self._date_type = date_type
