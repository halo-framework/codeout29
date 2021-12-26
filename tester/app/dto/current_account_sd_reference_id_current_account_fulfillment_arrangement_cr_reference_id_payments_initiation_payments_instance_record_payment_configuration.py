# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration_bill_pay_mandate_reference import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration_direct_debit_mandate_reference import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration_bill_pay_mandate_reference import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_initiation_payments_instance_record_payment_configuration_direct_debit_mandate_reference import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference  # noqa: E501



class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_schedule=None, direct_debit_mandate_reference=None, bill_pay_mandate_reference=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration - a model defined in OpenAPI

        :param payment_schedule: The payment_schedule of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.  # noqa: E501
        :type payment_schedule: str
        :param direct_debit_mandate_reference: The direct_debit_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.  # noqa: E501
        :type direct_debit_mandate_reference: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference
        :param bill_pay_mandate_reference: The bill_pay_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.  # noqa: E501
        :type bill_pay_mandate_reference: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
        """
        self.openapi_types = {
            'payment_schedule': str,
            'direct_debit_mandate_reference': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference,
            'bill_pay_mandate_reference': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
        }

        self.attribute_map = {
            'payment_schedule': 'paymentSchedule',
            'direct_debit_mandate_reference': 'directDebitMandateReference',
            'bill_pay_mandate_reference': 'billPayMandateReference'
        }

        self._payment_schedule = payment_schedule
        self._direct_debit_mandate_reference = direct_debit_mandate_reference
        self._bill_pay_mandate_reference = bill_pay_mandate_reference

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__payments_initiation_paymentsInstanceRecord_paymentConfiguration of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_schedule(self):
        """Gets the payment_schedule of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E7CIosTGEeChad0JzLk7QA_1664636213/elements/_E7CIpMTGEeChad0JzLk7QA_-1145087031  bian-reference: StandingOrderArrangement.StandingOrderSchedule  general-info: Processing schedule for repeating payments for standing orders (e.g. start date, end, period, number/cycles). Note this triggers an internal execution call as necessary   # noqa: E501

        :return: The payment_schedule of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :rtype: str
        """
        return self._payment_schedule

    @payment_schedule.setter
    def payment_schedule(self, payment_schedule):
        """Sets the payment_schedule of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E7CIosTGEeChad0JzLk7QA_1664636213/elements/_E7CIpMTGEeChad0JzLk7QA_-1145087031  bian-reference: StandingOrderArrangement.StandingOrderSchedule  general-info: Processing schedule for repeating payments for standing orders (e.g. start date, end, period, number/cycles). Note this triggers an internal execution call as necessary   # noqa: E501

        :param payment_schedule: The payment_schedule of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :type payment_schedule: str
        """

        self._payment_schedule = payment_schedule

    @property
    def direct_debit_mandate_reference(self):
        """Gets the direct_debit_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.


        :return: The direct_debit_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference
        """
        return self._direct_debit_mandate_reference

    @direct_debit_mandate_reference.setter
    def direct_debit_mandate_reference(self, direct_debit_mandate_reference):
        """Sets the direct_debit_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.


        :param direct_debit_mandate_reference: The direct_debit_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :type direct_debit_mandate_reference: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationDirectDebitMandateReference
        """

        self._direct_debit_mandate_reference = direct_debit_mandate_reference

    @property
    def bill_pay_mandate_reference(self):
        """Gets the bill_pay_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.


        :return: The bill_pay_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
        """
        return self._bill_pay_mandate_reference

    @bill_pay_mandate_reference.setter
    def bill_pay_mandate_reference(self, bill_pay_mandate_reference):
        """Sets the bill_pay_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.


        :param bill_pay_mandate_reference: The bill_pay_mandate_reference of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfiguration.
        :type bill_pay_mandate_reference: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsInitiationPaymentsInstanceRecordPaymentConfigurationBillPayMandateReference
        """

        self._bill_pay_mandate_reference = bill_pay_mandate_reference
