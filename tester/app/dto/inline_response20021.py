# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response20021_payments_instance_analysis import InlineResponse20021PaymentsInstanceAnalysis
from tester.app.dto.inline_response20021_payments_instance_record import InlineResponse20021PaymentsInstanceRecord
from tester.app.dto.inline_response20021_payments_instance_report import InlineResponse20021PaymentsInstanceReport
from tester import util

from tester.app.dto.inline_response20021_payments_instance_analysis import InlineResponse20021PaymentsInstanceAnalysis  # noqa: E501
from tester.app.dto.inline_response20021_payments_instance_record import InlineResponse20021PaymentsInstanceRecord  # noqa: E501
from tester.app.dto.inline_response20021_payments_instance_report import InlineResponse20021PaymentsInstanceReport  # noqa: E501



class InlineResponse20021(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payments_instance_record=None, payments_retrieve_action_task_reference=None, payments_retrieve_action_task_record=None, payments_retrieve_action_response=None, payments_instance_report=None, payments_instance_analysis=None):  # noqa: E501
        """InlineResponse20021 - a model defined in OpenAPI

        :param payments_instance_record: The payments_instance_record of this InlineResponse20021.  # noqa: E501
        :type payments_instance_record: InlineResponse20021PaymentsInstanceRecord
        :param payments_retrieve_action_task_reference: The payments_retrieve_action_task_reference of this InlineResponse20021.  # noqa: E501
        :type payments_retrieve_action_task_reference: str
        :param payments_retrieve_action_task_record: The payments_retrieve_action_task_record of this InlineResponse20021.  # noqa: E501
        :type payments_retrieve_action_task_record: object
        :param payments_retrieve_action_response: The payments_retrieve_action_response of this InlineResponse20021.  # noqa: E501
        :type payments_retrieve_action_response: str
        :param payments_instance_report: The payments_instance_report of this InlineResponse20021.  # noqa: E501
        :type payments_instance_report: InlineResponse20021PaymentsInstanceReport
        :param payments_instance_analysis: The payments_instance_analysis of this InlineResponse20021.  # noqa: E501
        :type payments_instance_analysis: InlineResponse20021PaymentsInstanceAnalysis
        """
        self.openapi_types = {
            'payments_instance_record': InlineResponse20021PaymentsInstanceRecord,
            'payments_retrieve_action_task_reference': str,
            'payments_retrieve_action_task_record': object,
            'payments_retrieve_action_response': str,
            'payments_instance_report': InlineResponse20021PaymentsInstanceReport,
            'payments_instance_analysis': InlineResponse20021PaymentsInstanceAnalysis
        }

        self.attribute_map = {
            'payments_instance_record': 'paymentsInstanceRecord',
            'payments_retrieve_action_task_reference': 'paymentsRetrieveActionTaskReference',
            'payments_retrieve_action_task_record': 'paymentsRetrieveActionTaskRecord',
            'payments_retrieve_action_response': 'paymentsRetrieveActionResponse',
            'payments_instance_report': 'paymentsInstanceReport',
            'payments_instance_analysis': 'paymentsInstanceAnalysis'
        }

        self._payments_instance_record = payments_instance_record
        self._payments_retrieve_action_task_reference = payments_retrieve_action_task_reference
        self._payments_retrieve_action_task_record = payments_retrieve_action_task_record
        self._payments_retrieve_action_response = payments_retrieve_action_response
        self._payments_instance_report = payments_instance_report
        self._payments_instance_analysis = payments_instance_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20021':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_21 of this InlineResponse20021.  # noqa: E501
        :rtype: InlineResponse20021
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payments_instance_record(self):
        """Gets the payments_instance_record of this InlineResponse20021.


        :return: The payments_instance_record of this InlineResponse20021.
        :rtype: InlineResponse20021PaymentsInstanceRecord
        """
        return self._payments_instance_record

    @payments_instance_record.setter
    def payments_instance_record(self, payments_instance_record):
        """Sets the payments_instance_record of this InlineResponse20021.


        :param payments_instance_record: The payments_instance_record of this InlineResponse20021.
        :type payments_instance_record: InlineResponse20021PaymentsInstanceRecord
        """

        self._payments_instance_record = payments_instance_record

    @property
    def payments_retrieve_action_task_reference(self):
        """Gets the payments_retrieve_action_task_reference of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Payments instance retrieve service call   # noqa: E501

        :return: The payments_retrieve_action_task_reference of this InlineResponse20021.
        :rtype: str
        """
        return self._payments_retrieve_action_task_reference

    @payments_retrieve_action_task_reference.setter
    def payments_retrieve_action_task_reference(self, payments_retrieve_action_task_reference):
        """Sets the payments_retrieve_action_task_reference of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Payments instance retrieve service call   # noqa: E501

        :param payments_retrieve_action_task_reference: The payments_retrieve_action_task_reference of this InlineResponse20021.
        :type payments_retrieve_action_task_reference: str
        """

        self._payments_retrieve_action_task_reference = payments_retrieve_action_task_reference

    @property
    def payments_retrieve_action_task_record(self):
        """Gets the payments_retrieve_action_task_record of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :return: The payments_retrieve_action_task_record of this InlineResponse20021.
        :rtype: object
        """
        return self._payments_retrieve_action_task_record

    @payments_retrieve_action_task_record.setter
    def payments_retrieve_action_task_record(self, payments_retrieve_action_task_record):
        """Sets the payments_retrieve_action_task_record of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :param payments_retrieve_action_task_record: The payments_retrieve_action_task_record of this InlineResponse20021.
        :type payments_retrieve_action_task_record: object
        """

        self._payments_retrieve_action_task_record = payments_retrieve_action_task_record

    @property
    def payments_retrieve_action_response(self):
        """Gets the payments_retrieve_action_response of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :return: The payments_retrieve_action_response of this InlineResponse20021.
        :rtype: str
        """
        return self._payments_retrieve_action_response

    @payments_retrieve_action_response.setter
    def payments_retrieve_action_response(self, payments_retrieve_action_response):
        """Sets the payments_retrieve_action_response of this InlineResponse20021.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :param payments_retrieve_action_response: The payments_retrieve_action_response of this InlineResponse20021.
        :type payments_retrieve_action_response: str
        """

        self._payments_retrieve_action_response = payments_retrieve_action_response

    @property
    def payments_instance_report(self):
        """Gets the payments_instance_report of this InlineResponse20021.


        :return: The payments_instance_report of this InlineResponse20021.
        :rtype: InlineResponse20021PaymentsInstanceReport
        """
        return self._payments_instance_report

    @payments_instance_report.setter
    def payments_instance_report(self, payments_instance_report):
        """Sets the payments_instance_report of this InlineResponse20021.


        :param payments_instance_report: The payments_instance_report of this InlineResponse20021.
        :type payments_instance_report: InlineResponse20021PaymentsInstanceReport
        """

        self._payments_instance_report = payments_instance_report

    @property
    def payments_instance_analysis(self):
        """Gets the payments_instance_analysis of this InlineResponse20021.


        :return: The payments_instance_analysis of this InlineResponse20021.
        :rtype: InlineResponse20021PaymentsInstanceAnalysis
        """
        return self._payments_instance_analysis

    @payments_instance_analysis.setter
    def payments_instance_analysis(self, payments_instance_analysis):
        """Sets the payments_instance_analysis of this InlineResponse20021.


        :param payments_instance_analysis: The payments_instance_analysis of this InlineResponse20021.
        :type payments_instance_analysis: InlineResponse20021PaymentsInstanceAnalysis
        """

        self._payments_instance_analysis = payments_instance_analysis
