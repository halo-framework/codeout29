# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response20020_payments_instance_record_payment_transaction import InlineResponse20020PaymentsInstanceRecordPaymentTransaction
from tester import util

from tester.app.dto.inline_response20020_payments_instance_record_payment_transaction import InlineResponse20020PaymentsInstanceRecordPaymentTransaction  # noqa: E501



class BQPaymentsExecuteOutputModelPaymentsInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_transaction=None):  # noqa: E501
        """BQPaymentsExecuteOutputModelPaymentsInstanceRecord - a model defined in OpenAPI

        :param payment_transaction: The payment_transaction of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.  # noqa: E501
        :type payment_transaction: InlineResponse20020PaymentsInstanceRecordPaymentTransaction
        """
        self.openapi_types = {
            'payment_transaction': InlineResponse20020PaymentsInstanceRecordPaymentTransaction
        }

        self.attribute_map = {
            'payment_transaction': 'paymentTransaction'
        }

        self._payment_transaction = payment_transaction

    @classmethod
    def from_dict(cls, dikt) -> 'BQPaymentsExecuteOutputModelPaymentsInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQPaymentsExecuteOutputModel_paymentsInstanceRecord of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.  # noqa: E501
        :rtype: BQPaymentsExecuteOutputModelPaymentsInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_transaction(self):
        """Gets the payment_transaction of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.


        :return: The payment_transaction of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.
        :rtype: InlineResponse20020PaymentsInstanceRecordPaymentTransaction
        """
        return self._payment_transaction

    @payment_transaction.setter
    def payment_transaction(self, payment_transaction):
        """Sets the payment_transaction of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.


        :param payment_transaction: The payment_transaction of this BQPaymentsExecuteOutputModelPaymentsInstanceRecord.
        :type payment_transaction: InlineResponse20020PaymentsInstanceRecordPaymentTransaction
        """

        self._payment_transaction = payment_transaction
