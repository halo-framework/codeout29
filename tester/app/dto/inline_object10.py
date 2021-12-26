# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_exchange_account_lien_exchange_action_request import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_exchange_account_lien_exchange_action_request import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest  # noqa: E501



class InlineObject10(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_reference=None, account_lien_instance_reference=None, account_lien_exchange_action_task_record=None, account_lien_exchange_action_request=None):  # noqa: E501
        """InlineObject10 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject10.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param account_lien_instance_reference: The account_lien_instance_reference of this InlineObject10.  # noqa: E501
        :type account_lien_instance_reference: str
        :param account_lien_exchange_action_task_record: The account_lien_exchange_action_task_record of this InlineObject10.  # noqa: E501
        :type account_lien_exchange_action_task_record: object
        :param account_lien_exchange_action_request: The account_lien_exchange_action_request of this InlineObject10.  # noqa: E501
        :type account_lien_exchange_action_request: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_reference': str,
            'account_lien_instance_reference': str,
            'account_lien_exchange_action_task_record': object,
            'account_lien_exchange_action_request': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'account_lien_instance_reference': 'accountLienInstanceReference',
            'account_lien_exchange_action_task_record': 'accountLienExchangeActionTaskRecord',
            'account_lien_exchange_action_request': 'accountLienExchangeActionRequest'
        }

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._account_lien_instance_reference = account_lien_instance_reference
        self._account_lien_exchange_action_task_record = account_lien_exchange_action_task_record
        self._account_lien_exchange_action_request = account_lien_exchange_action_request

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject10':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_10 of this InlineObject10.  # noqa: E501
        :rtype: InlineObject10
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this InlineObject10.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject10.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def account_lien_instance_reference(self):
        """Gets the account_lien_instance_reference of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :return: The account_lien_instance_reference of this InlineObject10.
        :rtype: str
        """
        return self._account_lien_instance_reference

    @account_lien_instance_reference.setter
    def account_lien_instance_reference(self, account_lien_instance_reference):
        """Sets the account_lien_instance_reference of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :param account_lien_instance_reference: The account_lien_instance_reference of this InlineObject10.
        :type account_lien_instance_reference: str
        """

        self._account_lien_instance_reference = account_lien_instance_reference

    @property
    def account_lien_exchange_action_task_record(self):
        """Gets the account_lien_exchange_action_task_record of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The exchange service call consolidated processing record   # noqa: E501

        :return: The account_lien_exchange_action_task_record of this InlineObject10.
        :rtype: object
        """
        return self._account_lien_exchange_action_task_record

    @account_lien_exchange_action_task_record.setter
    def account_lien_exchange_action_task_record(self, account_lien_exchange_action_task_record):
        """Sets the account_lien_exchange_action_task_record of this InlineObject10.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The exchange service call consolidated processing record   # noqa: E501

        :param account_lien_exchange_action_task_record: The account_lien_exchange_action_task_record of this InlineObject10.
        :type account_lien_exchange_action_task_record: object
        """

        self._account_lien_exchange_action_task_record = account_lien_exchange_action_task_record

    @property
    def account_lien_exchange_action_request(self):
        """Gets the account_lien_exchange_action_request of this InlineObject10.


        :return: The account_lien_exchange_action_request of this InlineObject10.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest
        """
        return self._account_lien_exchange_action_request

    @account_lien_exchange_action_request.setter
    def account_lien_exchange_action_request(self, account_lien_exchange_action_request):
        """Sets the account_lien_exchange_action_request of this InlineObject10.


        :param account_lien_exchange_action_request: The account_lien_exchange_action_request of this InlineObject10.
        :type account_lien_exchange_action_request: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdExchangeAccountLienExchangeActionRequest
        """

        self._account_lien_exchange_action_request = account_lien_exchange_action_request
