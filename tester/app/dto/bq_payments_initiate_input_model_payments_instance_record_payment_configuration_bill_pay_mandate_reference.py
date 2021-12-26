# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bill_pay_mandate_settings=None):  # noqa: E501
        """BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference - a model defined in OpenAPI

        :param bill_pay_mandate_settings: The bill_pay_mandate_settings of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.  # noqa: E501
        :type bill_pay_mandate_settings: str
        """
        self.openapi_types = {
            'bill_pay_mandate_settings': str
        }

        self.attribute_map = {
            'bill_pay_mandate_settings': 'billPayMandateSettings'
        }

        self._bill_pay_mandate_settings = bill_pay_mandate_settings

    @classmethod
    def from_dict(cls, dikt) -> 'BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQPaymentsInitiateInputModel_paymentsInstanceRecord_paymentConfiguration_billPayMandateReference of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.  # noqa: E501
        :rtype: BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bill_pay_mandate_settings(self):
        """Gets the bill_pay_mandate_settings of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Processing settings governing bill pay transactions   # noqa: E501

        :return: The bill_pay_mandate_settings of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.
        :rtype: str
        """
        return self._bill_pay_mandate_settings

    @bill_pay_mandate_settings.setter
    def bill_pay_mandate_settings(self, bill_pay_mandate_settings):
        """Sets the bill_pay_mandate_settings of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Processing settings governing bill pay transactions   # noqa: E501

        :param bill_pay_mandate_settings: The bill_pay_mandate_settings of this BQPaymentsInitiateInputModelPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference.
        :type bill_pay_mandate_settings: str
        """

        self._bill_pay_mandate_settings = bill_pay_mandate_settings