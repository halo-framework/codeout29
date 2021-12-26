# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, direct_debit_mandate_settings=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference - a model defined in OpenAPI

        :param direct_debit_mandate_settings: The direct_debit_mandate_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.  # noqa: E501
        :type direct_debit_mandate_settings: str
        """
        self.openapi_types = {
            'direct_debit_mandate_settings': str
        }

        self.attribute_map = {
            'direct_debit_mandate_settings': 'directDebitMandateSettings'
        }

        self._direct_debit_mandate_settings = direct_debit_mandate_settings

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__payments_initiation_paymentsInstanceRecord_paymentConfiguration_directDebitMandateReference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def direct_debit_mandate_settings(self):
        """Gets the direct_debit_mandate_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Processing settings governing direct debits   # noqa: E501

        :return: The direct_debit_mandate_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.
        :rtype: str
        """
        return self._direct_debit_mandate_settings

    @direct_debit_mandate_settings.setter
    def direct_debit_mandate_settings(self, direct_debit_mandate_settings):
        """Sets the direct_debit_mandate_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Processing settings governing direct debits   # noqa: E501

        :param direct_debit_mandate_settings: The direct_debit_mandate_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference.
        :type direct_debit_mandate_settings: str
        """

        self._direct_debit_mandate_settings = direct_debit_mandate_settings
