# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_update_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_update_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord  # noqa: E501



class InlineResponse2009(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_lien_instance_record=None, account_lien_update_action_task_reference=None, account_lien_update_action_task_record=None, update_response_record=None):  # noqa: E501
        """InlineResponse2009 - a model defined in OpenAPI

        :param account_lien_instance_record: The account_lien_instance_record of this InlineResponse2009.  # noqa: E501
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        :param account_lien_update_action_task_reference: The account_lien_update_action_task_reference of this InlineResponse2009.  # noqa: E501
        :type account_lien_update_action_task_reference: str
        :param account_lien_update_action_task_record: The account_lien_update_action_task_record of this InlineResponse2009.  # noqa: E501
        :type account_lien_update_action_task_record: object
        :param update_response_record: The update_response_record of this InlineResponse2009.  # noqa: E501
        :type update_response_record: object
        """
        self.openapi_types = {
            'account_lien_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord,
            'account_lien_update_action_task_reference': str,
            'account_lien_update_action_task_record': object,
            'update_response_record': object
        }

        self.attribute_map = {
            'account_lien_instance_record': 'accountLienInstanceRecord',
            'account_lien_update_action_task_reference': 'accountLienUpdateActionTaskReference',
            'account_lien_update_action_task_record': 'accountLienUpdateActionTaskRecord',
            'update_response_record': 'updateResponseRecord'
        }

        self._account_lien_instance_record = account_lien_instance_record
        self._account_lien_update_action_task_reference = account_lien_update_action_task_reference
        self._account_lien_update_action_task_record = account_lien_update_action_task_record
        self._update_response_record = update_response_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2009':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_9 of this InlineResponse2009.  # noqa: E501
        :rtype: InlineResponse2009
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_lien_instance_record(self):
        """Gets the account_lien_instance_record of this InlineResponse2009.


        :return: The account_lien_instance_record of this InlineResponse2009.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        """
        return self._account_lien_instance_record

    @account_lien_instance_record.setter
    def account_lien_instance_record(self, account_lien_instance_record):
        """Sets the account_lien_instance_record of this InlineResponse2009.


        :param account_lien_instance_record: The account_lien_instance_record of this InlineResponse2009.
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        """

        self._account_lien_instance_record = account_lien_instance_record

    @property
    def account_lien_update_action_task_reference(self):
        """Gets the account_lien_update_action_task_reference of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :return: The account_lien_update_action_task_reference of this InlineResponse2009.
        :rtype: str
        """
        return self._account_lien_update_action_task_reference

    @account_lien_update_action_task_reference.setter
    def account_lien_update_action_task_reference(self, account_lien_update_action_task_reference):
        """Sets the account_lien_update_action_task_reference of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :param account_lien_update_action_task_reference: The account_lien_update_action_task_reference of this InlineResponse2009.
        :type account_lien_update_action_task_reference: str
        """

        self._account_lien_update_action_task_reference = account_lien_update_action_task_reference

    @property
    def account_lien_update_action_task_record(self):
        """Gets the account_lien_update_action_task_record of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The account_lien_update_action_task_record of this InlineResponse2009.
        :rtype: object
        """
        return self._account_lien_update_action_task_record

    @account_lien_update_action_task_record.setter
    def account_lien_update_action_task_record(self, account_lien_update_action_task_record):
        """Sets the account_lien_update_action_task_record of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param account_lien_update_action_task_record: The account_lien_update_action_task_record of this InlineResponse2009.
        :type account_lien_update_action_task_record: object
        """

        self._account_lien_update_action_task_record = account_lien_update_action_task_record

    @property
    def update_response_record(self):
        """Gets the update_response_record of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :return: The update_response_record of this InlineResponse2009.
        :rtype: object
        """
        return self._update_response_record

    @update_response_record.setter
    def update_response_record(self, update_response_record):
        """Sets the update_response_record of this InlineResponse2009.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :param update_response_record: The update_response_record of this InlineResponse2009.
        :type update_response_record: object
        """

        self._update_response_record = update_response_record
