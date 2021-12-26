# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_account_lien_instance_record_lien_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_accountlien_initiation_account_lien_instance_record_lien_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord  # noqa: E501



class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lien_type=None, lien_definition=None, lien_processing_option=None, lien_record=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord - a model defined in OpenAPI

        :param lien_type: The lien_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.  # noqa: E501
        :type lien_type: str
        :param lien_definition: The lien_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.  # noqa: E501
        :type lien_definition: str
        :param lien_processing_option: The lien_processing_option of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.  # noqa: E501
        :type lien_processing_option: str
        :param lien_record: The lien_record of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.  # noqa: E501
        :type lien_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord
        """
        self.openapi_types = {
            'lien_type': str,
            'lien_definition': str,
            'lien_processing_option': str,
            'lien_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord
        }

        self.attribute_map = {
            'lien_type': 'lienType',
            'lien_definition': 'lienDefinition',
            'lien_processing_option': 'lienProcessingOption',
            'lien_record': 'lienRecord'
        }

        self._lien_type = lien_type
        self._lien_definition = lien_definition
        self._lien_processing_option = lien_processing_option
        self._lien_record = lien_record

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__accountlien_initiation_accountLienInstanceRecord of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lien_type(self):
        """Gets the lien_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of lien (e.g. final, pending)   # noqa: E501

        :return: The lien_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :rtype: str
        """
        return self._lien_type

    @lien_type.setter
    def lien_type(self, lien_type):
        """Sets the lien_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of lien (e.g. final, pending)   # noqa: E501

        :param lien_type: The lien_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :type lien_type: str
        """

        self._lien_type = lien_type

    @property
    def lien_definition(self):
        """Gets the lien_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the type of lien including processing guidelines   # noqa: E501

        :return: The lien_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :rtype: str
        """
        return self._lien_definition

    @lien_definition.setter
    def lien_definition(self, lien_definition):
        """Sets the lien_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the type of lien including processing guidelines   # noqa: E501

        :param lien_definition: The lien_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :type lien_definition: str
        """

        self._lien_definition = lien_definition

    @property
    def lien_processing_option(self):
        """Gets the lien_processing_option of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option applied to the lien   # noqa: E501

        :return: The lien_processing_option of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :rtype: str
        """
        return self._lien_processing_option

    @lien_processing_option.setter
    def lien_processing_option(self, lien_processing_option):
        """Sets the lien_processing_option of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option applied to the lien   # noqa: E501

        :param lien_processing_option: The lien_processing_option of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :type lien_processing_option: str
        """

        self._lien_processing_option = lien_processing_option

    @property
    def lien_record(self):
        """Gets the lien_record of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.


        :return: The lien_record of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord
        """
        return self._lien_record

    @lien_record.setter
    def lien_record(self, lien_record):
        """Sets the lien_record of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.


        :param lien_record: The lien_record of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecord.
        :type lien_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdAccountlienInitiationAccountLienInstanceRecordLienRecord
        """

        self._lien_record = lien_record
