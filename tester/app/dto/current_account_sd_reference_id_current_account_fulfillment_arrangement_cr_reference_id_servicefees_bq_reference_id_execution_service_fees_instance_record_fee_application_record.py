# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_accrual_amount import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_projectionsand_commitments import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_transaction import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_accrual_amount import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_projectionsand_commitments import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_service_fees_instance_record_fee_application_record_fee_transaction import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction  # noqa: E501



class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fee_transaction=None, fee_projectionsand_commitments=None, fee_accrual_amount=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord - a model defined in OpenAPI

        :param fee_transaction: The fee_transaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.  # noqa: E501
        :type fee_transaction: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction
        :param fee_projectionsand_commitments: The fee_projectionsand_commitments of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.  # noqa: E501
        :type fee_projectionsand_commitments: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments
        :param fee_accrual_amount: The fee_accrual_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.  # noqa: E501
        :type fee_accrual_amount: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount
        """
        self.openapi_types = {
            'fee_transaction': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction,
            'fee_projectionsand_commitments': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments,
            'fee_accrual_amount': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount
        }

        self.attribute_map = {
            'fee_transaction': 'feeTransaction',
            'fee_projectionsand_commitments': 'feeProjectionsandCommitments',
            'fee_accrual_amount': 'feeAccrualAmount'
        }

        self._fee_transaction = fee_transaction
        self._fee_projectionsand_commitments = fee_projectionsand_commitments
        self._fee_accrual_amount = fee_accrual_amount

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__servicefees__bq_reference_id__execution_serviceFeesInstanceRecord_feeApplicationRecord of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fee_transaction(self):
        """Gets the fee_transaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :return: The fee_transaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction
        """
        return self._fee_transaction

    @fee_transaction.setter
    def fee_transaction(self, fee_transaction):
        """Sets the fee_transaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :param fee_transaction: The fee_transaction of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :type fee_transaction: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeTransaction
        """

        self._fee_transaction = fee_transaction

    @property
    def fee_projectionsand_commitments(self):
        """Gets the fee_projectionsand_commitments of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :return: The fee_projectionsand_commitments of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments
        """
        return self._fee_projectionsand_commitments

    @fee_projectionsand_commitments.setter
    def fee_projectionsand_commitments(self, fee_projectionsand_commitments):
        """Sets the fee_projectionsand_commitments of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :param fee_projectionsand_commitments: The fee_projectionsand_commitments of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :type fee_projectionsand_commitments: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments
        """

        self._fee_projectionsand_commitments = fee_projectionsand_commitments

    @property
    def fee_accrual_amount(self):
        """Gets the fee_accrual_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :return: The fee_accrual_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount
        """
        return self._fee_accrual_amount

    @fee_accrual_amount.setter
    def fee_accrual_amount(self, fee_accrual_amount):
        """Sets the fee_accrual_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.


        :param fee_accrual_amount: The fee_accrual_amount of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecord.
        :type fee_accrual_amount: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionServiceFeesInstanceRecordFeeApplicationRecordFeeAccrualAmount
        """

        self._fee_accrual_amount = fee_accrual_amount
