# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse20020PaymentsInstanceRecordPaymentTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_transaction_date=None, payment_transaction_status=None):  # noqa: E501
        """InlineResponse20020PaymentsInstanceRecordPaymentTransaction - a model defined in OpenAPI

        :param payment_transaction_date: The payment_transaction_date of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_date: str
        :param payment_transaction_status: The payment_transaction_status of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_status: str
        """
        self.openapi_types = {
            'payment_transaction_date': str,
            'payment_transaction_status': str
        }

        self.attribute_map = {
            'payment_transaction_date': 'paymentTransactionDate',
            'payment_transaction_status': 'paymentTransactionStatus'
        }

        self._payment_transaction_date = payment_transaction_date
        self._payment_transaction_status = payment_transaction_status

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20020PaymentsInstanceRecordPaymentTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_20_paymentsInstanceRecord_paymentTransaction of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :rtype: InlineResponse20020PaymentsInstanceRecordPaymentTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_transaction_date(self):
        """Gets the payment_transaction_date of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FDYMU8TGEeChad0JzLk7QA_1746210992  bian-reference: PaymentTransactionValueDate  general-info: The various key dates and times associated with the payment transaction   # noqa: E501

        :return: The payment_transaction_date of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_date

    @payment_transaction_date.setter
    def payment_transaction_date(self, payment_transaction_date):
        """Sets the payment_transaction_date of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FDYMU8TGEeChad0JzLk7QA_1746210992  bian-reference: PaymentTransactionValueDate  general-info: The various key dates and times associated with the payment transaction   # noqa: E501

        :param payment_transaction_date: The payment_transaction_date of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_date: str
        """

        self._payment_transaction_date = payment_transaction_date

    @property
    def payment_transaction_status(self):
        """Gets the payment_transaction_status of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FCe0dcTGEeChad0JzLk7QA_221546661  bian-reference: BankingTransactionStatus  general-info: The processing status of the transaction (e.g. captured, approved, initiated, confirmed, settled)   # noqa: E501

        :return: The payment_transaction_status of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_status

    @payment_transaction_status.setter
    def payment_transaction_status(self, payment_transaction_status):
        """Sets the payment_transaction_status of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FCe0dcTGEeChad0JzLk7QA_221546661  bian-reference: BankingTransactionStatus  general-info: The processing status of the transaction (e.g. captured, approved, initiated, confirmed, settled)   # noqa: E501

        :param payment_transaction_status: The payment_transaction_status of this InlineResponse20020PaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_status: str
        """

        self._payment_transaction_status = payment_transaction_status
