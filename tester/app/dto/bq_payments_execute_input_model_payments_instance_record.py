# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution_payments_instance_record_payment_transaction import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution_payments_instance_record_payment_transaction import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction  # noqa: E501



class BQPaymentsExecuteInputModelPaymentsInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_transaction=None):  # noqa: E501
        """BQPaymentsExecuteInputModelPaymentsInstanceRecord - a model defined in OpenAPI

        :param payment_transaction: The payment_transaction of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_transaction: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction
        """
        self.openapi_types = {
            'payment_transaction': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction
        }

        self.attribute_map = {
            'payment_transaction': 'paymentTransaction'
        }

        self._payment_transaction = payment_transaction

    @classmethod
    def from_dict(cls, dikt) -> 'BQPaymentsExecuteInputModelPaymentsInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQPaymentsExecuteInputModel_paymentsInstanceRecord of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.  # noqa: E501
        :rtype: BQPaymentsExecuteInputModelPaymentsInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_transaction(self):
        """Gets the payment_transaction of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.


        :return: The payment_transaction of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction
        """
        return self._payment_transaction

    @payment_transaction.setter
    def payment_transaction(self, payment_transaction):
        """Sets the payment_transaction of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.


        :param payment_transaction: The payment_transaction of this BQPaymentsExecuteInputModelPaymentsInstanceRecord.
        :type payment_transaction: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecordPaymentTransaction
        """

        self._payment_transaction = payment_transaction