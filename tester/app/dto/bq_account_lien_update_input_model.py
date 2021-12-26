# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_update_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_bq_reference_id_update_account_lien_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord  # noqa: E501



class BQAccountLienUpdateInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_reference=None, account_lien_instance_reference=None, account_lien_instance_record=None, account_lien_update_action_task_record=None, account_lien_update_action_request=None):  # noqa: E501
        """BQAccountLienUpdateInputModel - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this BQAccountLienUpdateInputModel.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param account_lien_instance_reference: The account_lien_instance_reference of this BQAccountLienUpdateInputModel.  # noqa: E501
        :type account_lien_instance_reference: str
        :param account_lien_instance_record: The account_lien_instance_record of this BQAccountLienUpdateInputModel.  # noqa: E501
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        :param account_lien_update_action_task_record: The account_lien_update_action_task_record of this BQAccountLienUpdateInputModel.  # noqa: E501
        :type account_lien_update_action_task_record: object
        :param account_lien_update_action_request: The account_lien_update_action_request of this BQAccountLienUpdateInputModel.  # noqa: E501
        :type account_lien_update_action_request: str
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_reference': str,
            'account_lien_instance_reference': str,
            'account_lien_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord,
            'account_lien_update_action_task_record': object,
            'account_lien_update_action_request': str
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'account_lien_instance_reference': 'accountLienInstanceReference',
            'account_lien_instance_record': 'accountLienInstanceRecord',
            'account_lien_update_action_task_record': 'accountLienUpdateActionTaskRecord',
            'account_lien_update_action_request': 'accountLienUpdateActionRequest'
        }

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._account_lien_instance_reference = account_lien_instance_reference
        self._account_lien_instance_record = account_lien_instance_record
        self._account_lien_update_action_task_record = account_lien_update_action_task_record
        self._account_lien_update_action_request = account_lien_update_action_request

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountLienUpdateInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountLienUpdateInputModel of this BQAccountLienUpdateInputModel.  # noqa: E501
        :rtype: BQAccountLienUpdateInputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this BQAccountLienUpdateInputModel.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this BQAccountLienUpdateInputModel.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def account_lien_instance_reference(self):
        """Gets the account_lien_instance_reference of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :return: The account_lien_instance_reference of this BQAccountLienUpdateInputModel.
        :rtype: str
        """
        return self._account_lien_instance_reference

    @account_lien_instance_reference.setter
    def account_lien_instance_reference(self, account_lien_instance_reference):
        """Sets the account_lien_instance_reference of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Account Lien instance   # noqa: E501

        :param account_lien_instance_reference: The account_lien_instance_reference of this BQAccountLienUpdateInputModel.
        :type account_lien_instance_reference: str
        """

        self._account_lien_instance_reference = account_lien_instance_reference

    @property
    def account_lien_instance_record(self):
        """Gets the account_lien_instance_record of this BQAccountLienUpdateInputModel.


        :return: The account_lien_instance_record of this BQAccountLienUpdateInputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        """
        return self._account_lien_instance_record

    @account_lien_instance_record.setter
    def account_lien_instance_record(self, account_lien_instance_record):
        """Sets the account_lien_instance_record of this BQAccountLienUpdateInputModel.


        :param account_lien_instance_record: The account_lien_instance_record of this BQAccountLienUpdateInputModel.
        :type account_lien_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienBqReferenceIdUpdateAccountLienInstanceRecord
        """

        self._account_lien_instance_record = account_lien_instance_record

    @property
    def account_lien_update_action_task_record(self):
        """Gets the account_lien_update_action_task_record of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The account_lien_update_action_task_record of this BQAccountLienUpdateInputModel.
        :rtype: object
        """
        return self._account_lien_update_action_task_record

    @account_lien_update_action_task_record.setter
    def account_lien_update_action_task_record(self, account_lien_update_action_task_record):
        """Sets the account_lien_update_action_task_record of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param account_lien_update_action_task_record: The account_lien_update_action_task_record of this BQAccountLienUpdateInputModel.
        :type account_lien_update_action_task_record: object
        """

        self._account_lien_update_action_task_record = account_lien_update_action_task_record

    @property
    def account_lien_update_action_request(self):
        """Gets the account_lien_update_action_request of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :return: The account_lien_update_action_request of this BQAccountLienUpdateInputModel.
        :rtype: str
        """
        return self._account_lien_update_action_request

    @account_lien_update_action_request.setter
    def account_lien_update_action_request(self, account_lien_update_action_request):
        """Sets the account_lien_update_action_request of this BQAccountLienUpdateInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the update action service request   # noqa: E501

        :param account_lien_update_action_request: The account_lien_update_action_request of this BQAccountLienUpdateInputModel.
        :type account_lien_update_action_request: str
        """

        self._account_lien_update_action_request = account_lien_update_action_request
