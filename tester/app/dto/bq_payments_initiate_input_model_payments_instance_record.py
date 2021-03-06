# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration  # noqa: E501



class BQPaymentsInitiateInputModelPaymentsInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_type=None, payment_definition=None, payment_processing_option_setting=None, payment_configuration=None):  # noqa: E501
        """BQPaymentsInitiateInputModelPaymentsInstanceRecord - a model defined in OpenAPI

        :param payment_type: The payment_type of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_type: str
        :param payment_definition: The payment_definition of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_definition: str
        :param payment_processing_option_setting: The payment_processing_option_setting of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_processing_option_setting: str
        :param payment_configuration: The payment_configuration of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_configuration: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
        """
        self.openapi_types = {
            'payment_type': str,
            'payment_definition': str,
            'payment_processing_option_setting': str,
            'payment_configuration': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
        }

        self.attribute_map = {
            'payment_type': 'paymentType',
            'payment_definition': 'paymentDefinition',
            'payment_processing_option_setting': 'paymentProcessingOptionSetting',
            'payment_configuration': 'paymentConfiguration'
        }

        self._payment_type = payment_type
        self._payment_definition = payment_definition
        self._payment_processing_option_setting = payment_processing_option_setting
        self._payment_configuration = payment_configuration

    @classmethod
    def from_dict(cls, dikt) -> 'BQPaymentsInitiateInputModelPaymentsInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQPaymentsInitiateInputModel_paymentsInstanceRecord of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.  # noqa: E501
        :rtype: BQPaymentsInitiateInputModelPaymentsInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_type(self):
        """Gets the payment_type of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FColc8TGEeChad0JzLk7QA_1437769975  bian-reference: PaymentService.PaymentType  general-info: The type of payment transaction (e.g. customer payment, standing order, direct debit, bill pay)   # noqa: E501

        :return: The payment_type of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FColc8TGEeChad0JzLk7QA_1437769975  bian-reference: PaymentService.PaymentType  general-info: The type of payment transaction (e.g. customer payment, standing order, direct debit, bill pay)   # noqa: E501

        :param payment_type: The payment_type of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :type payment_type: str
        """

        self._payment_type = payment_type

    @property
    def payment_definition(self):
        """Gets the payment_definition of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FDPCYMTGEeChad0JzLk7QA_-1131921749/elements/_FDYMUMTGEeChad0JzLk7QA_-1392150264  bian-reference: PaymentService.PaymentDefinition  general-info: Definition of the type of payment including processing rules and guidelines   # noqa: E501

        :return: The payment_definition of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :rtype: str
        """
        return self._payment_definition

    @payment_definition.setter
    def payment_definition(self, payment_definition):
        """Sets the payment_definition of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FDPCYMTGEeChad0JzLk7QA_-1131921749/elements/_FDYMUMTGEeChad0JzLk7QA_-1392150264  bian-reference: PaymentService.PaymentDefinition  general-info: Definition of the type of payment including processing rules and guidelines   # noqa: E501

        :param payment_definition: The payment_definition of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :type payment_definition: str
        """

        self._payment_definition = payment_definition

    @property
    def payment_processing_option_setting(self):
        """Gets the payment_processing_option_setting of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The option setting   # noqa: E501

        :return: The payment_processing_option_setting of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :rtype: str
        """
        return self._payment_processing_option_setting

    @payment_processing_option_setting.setter
    def payment_processing_option_setting(self, payment_processing_option_setting):
        """Sets the payment_processing_option_setting of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The option setting   # noqa: E501

        :param payment_processing_option_setting: The payment_processing_option_setting of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :type payment_processing_option_setting: str
        """

        self._payment_processing_option_setting = payment_processing_option_setting

    @property
    def payment_configuration(self):
        """Gets the payment_configuration of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.


        :return: The payment_configuration of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
        """
        return self._payment_configuration

    @payment_configuration.setter
    def payment_configuration(self, payment_configuration):
        """Sets the payment_configuration of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.


        :param payment_configuration: The payment_configuration of this BQPaymentsInitiateInputModelPaymentsInstanceRecord.
        :type payment_configuration: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
        """

        self._payment_configuration = payment_configuration
