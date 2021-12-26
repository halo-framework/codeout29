# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution_payments_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_execute_record_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_payments_bq_reference_id_execution_payments_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_servicefees_bq_reference_id_execution_execute_record_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType  # noqa: E501



class InlineObject20(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_account_fulfillment_arrangement_instance_reference=None, payments_instance_reference=None, payments_instance_record=None, payments_execute_action_task_record=None, execute_record_type=None):  # noqa: E501
        """InlineObject20 - a model defined in OpenAPI

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject20.  # noqa: E501
        :type current_account_fulfillment_arrangement_instance_reference: str
        :param payments_instance_reference: The payments_instance_reference of this InlineObject20.  # noqa: E501
        :type payments_instance_reference: str
        :param payments_instance_record: The payments_instance_record of this InlineObject20.  # noqa: E501
        :type payments_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord
        :param payments_execute_action_task_record: The payments_execute_action_task_record of this InlineObject20.  # noqa: E501
        :type payments_execute_action_task_record: object
        :param execute_record_type: The execute_record_type of this InlineObject20.  # noqa: E501
        :type execute_record_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType
        """
        self.openapi_types = {
            'current_account_fulfillment_arrangement_instance_reference': str,
            'payments_instance_reference': str,
            'payments_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord,
            'payments_execute_action_task_record': object,
            'execute_record_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType
        }

        self.attribute_map = {
            'current_account_fulfillment_arrangement_instance_reference': 'currentAccountFulfillmentArrangementInstanceReference',
            'payments_instance_reference': 'paymentsInstanceReference',
            'payments_instance_record': 'paymentsInstanceRecord',
            'payments_execute_action_task_record': 'paymentsExecuteActionTaskRecord',
            'execute_record_type': 'executeRecordType'
        }

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference
        self._payments_instance_reference = payments_instance_reference
        self._payments_instance_record = payments_instance_record
        self._payments_execute_action_task_record = payments_execute_action_task_record
        self._execute_record_type = execute_record_type

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject20':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_20 of this InlineObject20.  # noqa: E501
        :rtype: InlineObject20
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_account_fulfillment_arrangement_instance_reference(self):
        """Gets the current_account_fulfillment_arrangement_instance_reference of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :return: The current_account_fulfillment_arrangement_instance_reference of this InlineObject20.
        :rtype: str
        """
        return self._current_account_fulfillment_arrangement_instance_reference

    @current_account_fulfillment_arrangement_instance_reference.setter
    def current_account_fulfillment_arrangement_instance_reference(self, current_account_fulfillment_arrangement_instance_reference):
        """Sets the current_account_fulfillment_arrangement_instance_reference of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the parent Current Account Fulfillment Arrangement instance   # noqa: E501

        :param current_account_fulfillment_arrangement_instance_reference: The current_account_fulfillment_arrangement_instance_reference of this InlineObject20.
        :type current_account_fulfillment_arrangement_instance_reference: str
        """

        self._current_account_fulfillment_arrangement_instance_reference = current_account_fulfillment_arrangement_instance_reference

    @property
    def payments_instance_reference(self):
        """Gets the payments_instance_reference of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :return: The payments_instance_reference of this InlineObject20.
        :rtype: str
        """
        return self._payments_instance_reference

    @payments_instance_reference.setter
    def payments_instance_reference(self, payments_instance_reference):
        """Sets the payments_instance_reference of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments instance   # noqa: E501

        :param payments_instance_reference: The payments_instance_reference of this InlineObject20.
        :type payments_instance_reference: str
        """

        self._payments_instance_reference = payments_instance_reference

    @property
    def payments_instance_record(self):
        """Gets the payments_instance_record of this InlineObject20.


        :return: The payments_instance_record of this InlineObject20.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord
        """
        return self._payments_instance_record

    @payments_instance_record.setter
    def payments_instance_record(self, payments_instance_record):
        """Sets the payments_instance_record of this InlineObject20.


        :param payments_instance_record: The payments_instance_record of this InlineObject20.
        :type payments_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdPaymentsBqReferenceIdExecutionPaymentsInstanceRecord
        """

        self._payments_instance_record = payments_instance_record

    @property
    def payments_execute_action_task_record(self):
        """Gets the payments_execute_action_task_record of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The execute service call consolidated processing record   # noqa: E501

        :return: The payments_execute_action_task_record of this InlineObject20.
        :rtype: object
        """
        return self._payments_execute_action_task_record

    @payments_execute_action_task_record.setter
    def payments_execute_action_task_record(self, payments_execute_action_task_record):
        """Sets the payments_execute_action_task_record of this InlineObject20.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The execute service call consolidated processing record   # noqa: E501

        :param payments_execute_action_task_record: The payments_execute_action_task_record of this InlineObject20.
        :type payments_execute_action_task_record: object
        """

        self._payments_execute_action_task_record = payments_execute_action_task_record

    @property
    def execute_record_type(self):
        """Gets the execute_record_type of this InlineObject20.


        :return: The execute_record_type of this InlineObject20.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType
        """
        return self._execute_record_type

    @execute_record_type.setter
    def execute_record_type(self, execute_record_type):
        """Sets the execute_record_type of this InlineObject20.


        :param execute_record_type: The execute_record_type of this InlineObject20.
        :type execute_record_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesBqReferenceIdExecutionExecuteRecordType
        """

        self._execute_record_type = execute_record_type
