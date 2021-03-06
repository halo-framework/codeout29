# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response20020_payments_instance_record import InlineResponse20020PaymentsInstanceRecord
from tester import util

from tester.app.dto.inline_response20020_payments_instance_record import InlineResponse20020PaymentsInstanceRecord  # noqa: E501



class InlineResponse20020(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payments_instance_record=None, payments_execute_action_task_reference=None, payments_execute_action_task_record=None, payments_execute_record_reference=None, execute_response_record=None):  # noqa: E501
        """InlineResponse20020 - a model defined in OpenAPI

        :param payments_instance_record: The payments_instance_record of this InlineResponse20020.  # noqa: E501
        :type payments_instance_record: InlineResponse20020PaymentsInstanceRecord
        :param payments_execute_action_task_reference: The payments_execute_action_task_reference of this InlineResponse20020.  # noqa: E501
        :type payments_execute_action_task_reference: str
        :param payments_execute_action_task_record: The payments_execute_action_task_record of this InlineResponse20020.  # noqa: E501
        :type payments_execute_action_task_record: object
        :param payments_execute_record_reference: The payments_execute_record_reference of this InlineResponse20020.  # noqa: E501
        :type payments_execute_record_reference: str
        :param execute_response_record: The execute_response_record of this InlineResponse20020.  # noqa: E501
        :type execute_response_record: object
        """
        self.openapi_types = {
            'payments_instance_record': InlineResponse20020PaymentsInstanceRecord,
            'payments_execute_action_task_reference': str,
            'payments_execute_action_task_record': object,
            'payments_execute_record_reference': str,
            'execute_response_record': object
        }

        self.attribute_map = {
            'payments_instance_record': 'paymentsInstanceRecord',
            'payments_execute_action_task_reference': 'paymentsExecuteActionTaskReference',
            'payments_execute_action_task_record': 'paymentsExecuteActionTaskRecord',
            'payments_execute_record_reference': 'paymentsExecuteRecordReference',
            'execute_response_record': 'executeResponseRecord'
        }

        self._payments_instance_record = payments_instance_record
        self._payments_execute_action_task_reference = payments_execute_action_task_reference
        self._payments_execute_action_task_record = payments_execute_action_task_record
        self._payments_execute_record_reference = payments_execute_record_reference
        self._execute_response_record = execute_response_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20020':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_20 of this InlineResponse20020.  # noqa: E501
        :rtype: InlineResponse20020
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payments_instance_record(self):
        """Gets the payments_instance_record of this InlineResponse20020.


        :return: The payments_instance_record of this InlineResponse20020.
        :rtype: InlineResponse20020PaymentsInstanceRecord
        """
        return self._payments_instance_record

    @payments_instance_record.setter
    def payments_instance_record(self, payments_instance_record):
        """Sets the payments_instance_record of this InlineResponse20020.


        :param payments_instance_record: The payments_instance_record of this InlineResponse20020.
        :type payments_instance_record: InlineResponse20020PaymentsInstanceRecord
        """

        self._payments_instance_record = payments_instance_record

    @property
    def payments_execute_action_task_reference(self):
        """Gets the payments_execute_action_task_reference of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Payments instance execute service call   # noqa: E501

        :return: The payments_execute_action_task_reference of this InlineResponse20020.
        :rtype: str
        """
        return self._payments_execute_action_task_reference

    @payments_execute_action_task_reference.setter
    def payments_execute_action_task_reference(self, payments_execute_action_task_reference):
        """Sets the payments_execute_action_task_reference of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Payments instance execute service call   # noqa: E501

        :param payments_execute_action_task_reference: The payments_execute_action_task_reference of this InlineResponse20020.
        :type payments_execute_action_task_reference: str
        """

        self._payments_execute_action_task_reference = payments_execute_action_task_reference

    @property
    def payments_execute_action_task_record(self):
        """Gets the payments_execute_action_task_record of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The execute service call consolidated processing record   # noqa: E501

        :return: The payments_execute_action_task_record of this InlineResponse20020.
        :rtype: object
        """
        return self._payments_execute_action_task_record

    @payments_execute_action_task_record.setter
    def payments_execute_action_task_record(self, payments_execute_action_task_record):
        """Sets the payments_execute_action_task_record of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The execute service call consolidated processing record   # noqa: E501

        :param payments_execute_action_task_record: The payments_execute_action_task_record of this InlineResponse20020.
        :type payments_execute_action_task_record: object
        """

        self._payments_execute_action_task_record = payments_execute_action_task_record

    @property
    def payments_execute_record_reference(self):
        """Gets the payments_execute_record_reference of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments execute transaction/record   # noqa: E501

        :return: The payments_execute_record_reference of this InlineResponse20020.
        :rtype: str
        """
        return self._payments_execute_record_reference

    @payments_execute_record_reference.setter
    def payments_execute_record_reference(self, payments_execute_record_reference):
        """Sets the payments_execute_record_reference of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Payments execute transaction/record   # noqa: E501

        :param payments_execute_record_reference: The payments_execute_record_reference of this InlineResponse20020.
        :type payments_execute_record_reference: str
        """

        self._payments_execute_record_reference = payments_execute_record_reference

    @property
    def execute_response_record(self):
        """Gets the execute_response_record of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the execute action service response   # noqa: E501

        :return: The execute_response_record of this InlineResponse20020.
        :rtype: object
        """
        return self._execute_response_record

    @execute_response_record.setter
    def execute_response_record(self, execute_response_record):
        """Sets the execute_response_record of this InlineResponse20020.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the execute action service response   # noqa: E501

        :param execute_response_record: The execute_response_record of this InlineResponse20020.
        :type execute_response_record: object
        """

        self._execute_response_record = execute_response_record
