# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_current_account_fulfillment_arrangement_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord  # noqa: E501



class InlineObject8(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_record=None, current_account_fulfillment_arrangement_instance_reference=None, account_lien_initiate_action_record=None, account_lien_instance_record=None):  # noqa: E501
        """InlineObject8 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineObject8.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject8.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param account_lien_initiate_action_record: The account_lien_initiate_action_record of this InlineObject8.  # noqa: E501
        :type account_lien_initiate_action_record: object
        :param account_lien_instance_record: The account_lien_instance_record of this InlineObject8.  # noqa: E501
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord,
            'current_account_fulfillment_arrangement_instance_reference': str,
            'account_lien_initiate_action_record': object,
            'account_lien_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_record': 'currentAccountFulfillmentArrangementInstanceRecord',
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'account_lien_initiate_action_record': 'accountLienInitiateActionRecord',
            'account_lien_instance_record': 'accountLienInstanceRecord'
        }

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record
        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._account_lien_initiate_action_record = account_lien_initiate_action_record
        self._account_lien_instance_record = account_lien_instance_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject8':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_8 of this InlineObject8.  # noqa: E501
        :rtype: InlineObject8
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_record(self):
        """Gets the current_account_fulfillment_arrangement_instance_record of this InlineObject8.


        :return: The current_account_fulfillment_arrangement_instance_record of this InlineObject8.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return self._current_account_fulfillment_arrangement_instance_record

    @current_account_fulfillment_arrangement_instance_record.setter
    def current_account_fulfillment_arrangement_instance_record(self, current_account_fulfillment_arrangement_instance_record):
        """Sets the current_account_fulfillment_arrangement_instance_record of this InlineObject8.


        :param current_account_fulfillment_arrangement_instance_record: The current_account_fulfillment_arrangement_instance_record of this InlineObject8.
        :type current_account_fulfillment_arrangement_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationCurrentAccountFulfillmentArrangementInstanceRecord
        """

        self._current_account_fulfillment_arrangement_instance_record = current_account_fulfillment_arrangement_instance_record

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this InlineObject8.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this InlineObject8.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this InlineObject8.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject8.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def account_lien_initiate_action_record(self):
        """Gets the account_lien_initiate_action_record of this InlineObject8.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :return: The account_lien_initiate_action_record of this InlineObject8.
        :rtype: object
        """
        return self._account_lien_initiate_action_record

    @account_lien_initiate_action_record.setter
    def account_lien_initiate_action_record(self, account_lien_initiate_action_record):
        """Sets the account_lien_initiate_action_record of this InlineObject8.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The Initiate service call input and output record   # noqa: E501

        :param account_lien_initiate_action_record: The account_lien_initiate_action_record of this InlineObject8.
        :type account_lien_initiate_action_record: object
        """

        self._account_lien_initiate_action_record = account_lien_initiate_action_record

    @property
    def account_lien_instance_record(self):
        """Gets the account_lien_instance_record of this InlineObject8.


        :return: The account_lien_instance_record of this InlineObject8.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
        """
        return self._account_lien_instance_record

    @account_lien_instance_record.setter
    def account_lien_instance_record(self, account_lien_instance_record):
        """Sets the account_lien_instance_record of this InlineObject8.


        :param account_lien_instance_record: The account_lien_instance_record of this InlineObject8.
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
        """

        self._account_lien_instance_record = account_lien_instance_record