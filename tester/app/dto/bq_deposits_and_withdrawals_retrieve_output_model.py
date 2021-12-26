# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_analysis import InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record import InlineResponse20017DepositsAndWithdrawalsInstanceRecord
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_report import InlineResponse20017DepositsAndWithdrawalsInstanceReport
from tester import util

from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_analysis import InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis  # noqa: E501
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_record import InlineResponse20017DepositsAndWithdrawalsInstanceRecord  # noqa: E501
from tester.app.dto.inline_response20017_deposits_and_withdrawals_instance_report import InlineResponse20017DepositsAndWithdrawalsInstanceReport  # noqa: E501



class BQDepositsAndWithdrawalsRetrieveOutputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposits_and_withdrawals_instance_record=None, deposits_and_withdrawals_retrieve_action_task_reference=None, deposits_and_withdrawals_retrieve_action_task_record=None, deposits_and_withdrawals_retrieve_action_response=None, deposits_and_withdrawals_instance_report=None, deposits_and_withdrawals_instance_analysis=None):  # noqa: E501
        """BQDepositsAndWithdrawalsRetrieveOutputModel - a model defined in OpenAPI

        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_instance_record: InlineResponse20017DepositsAndWithdrawalsInstanceRecord
        :param deposits_and_withdrawals_retrieve_action_task_reference: The deposits_and_withdrawals_retrieve_action_task_reference of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_retrieve_action_task_reference: str
        :param deposits_and_withdrawals_retrieve_action_task_record: The deposits_and_withdrawals_retrieve_action_task_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_retrieve_action_task_record: object
        :param deposits_and_withdrawals_retrieve_action_response: The deposits_and_withdrawals_retrieve_action_response of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_retrieve_action_response: str
        :param deposits_and_withdrawals_instance_report: The deposits_and_withdrawals_instance_report of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_instance_report: InlineResponse20017DepositsAndWithdrawalsInstanceReport
        :param deposits_and_withdrawals_instance_analysis: The deposits_and_withdrawals_instance_analysis of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :type deposits_and_withdrawals_instance_analysis: InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
        """
        self.openapi_types = {
            'deposits_and_withdrawals_instance_record': InlineResponse20017DepositsAndWithdrawalsInstanceRecord,
            'deposits_and_withdrawals_retrieve_action_task_reference': str,
            'deposits_and_withdrawals_retrieve_action_task_record': object,
            'deposits_and_withdrawals_retrieve_action_response': str,
            'deposits_and_withdrawals_instance_report': InlineResponse20017DepositsAndWithdrawalsInstanceReport,
            'deposits_and_withdrawals_instance_analysis': InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
        }

        self.attribute_map = {
            'deposits_and_withdrawals_instance_record': 'depositsAndWithdrawalsInstanceRecord',
            'deposits_and_withdrawals_retrieve_action_task_reference': 'depositsAndWithdrawalsRetrieveActionTaskReference',
            'deposits_and_withdrawals_retrieve_action_task_record': 'depositsAndWithdrawalsRetrieveActionTaskRecord',
            'deposits_and_withdrawals_retrieve_action_response': 'depositsAndWithdrawalsRetrieveActionResponse',
            'deposits_and_withdrawals_instance_report': 'depositsAndWithdrawalsInstanceReport',
            'deposits_and_withdrawals_instance_analysis': 'depositsAndWithdrawalsInstanceAnalysis'
        }

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record
        self._deposits_and_withdrawals_retrieve_action_task_reference = deposits_and_withdrawals_retrieve_action_task_reference
        self._deposits_and_withdrawals_retrieve_action_task_record = deposits_and_withdrawals_retrieve_action_task_record
        self._deposits_and_withdrawals_retrieve_action_response = deposits_and_withdrawals_retrieve_action_response
        self._deposits_and_withdrawals_instance_report = deposits_and_withdrawals_instance_report
        self._deposits_and_withdrawals_instance_analysis = deposits_and_withdrawals_instance_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsRetrieveOutputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsRetrieveOutputModel of this BQDepositsAndWithdrawalsRetrieveOutputModel.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsRetrieveOutputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposits_and_withdrawals_instance_record(self):
        """Gets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :return: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceRecord
        """
        return self._deposits_and_withdrawals_instance_record

    @deposits_and_withdrawals_instance_record.setter
    def deposits_and_withdrawals_instance_record(self, deposits_and_withdrawals_instance_record):
        """Sets the deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :param deposits_and_withdrawals_instance_record: The deposits_and_withdrawals_instance_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_instance_record: InlineResponse20017DepositsAndWithdrawalsInstanceRecord
        """

        self._deposits_and_withdrawals_instance_record = deposits_and_withdrawals_instance_record

    @property
    def deposits_and_withdrawals_retrieve_action_task_reference(self):
        """Gets the deposits_and_withdrawals_retrieve_action_task_reference of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Deposits And Withdrawals instance retrieve service call   # noqa: E501

        :return: The deposits_and_withdrawals_retrieve_action_task_reference of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: str
        """
        return self._deposits_and_withdrawals_retrieve_action_task_reference

    @deposits_and_withdrawals_retrieve_action_task_reference.setter
    def deposits_and_withdrawals_retrieve_action_task_reference(self, deposits_and_withdrawals_retrieve_action_task_reference):
        """Sets the deposits_and_withdrawals_retrieve_action_task_reference of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Deposits And Withdrawals instance retrieve service call   # noqa: E501

        :param deposits_and_withdrawals_retrieve_action_task_reference: The deposits_and_withdrawals_retrieve_action_task_reference of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_retrieve_action_task_reference: str
        """

        self._deposits_and_withdrawals_retrieve_action_task_reference = deposits_and_withdrawals_retrieve_action_task_reference

    @property
    def deposits_and_withdrawals_retrieve_action_task_record(self):
        """Gets the deposits_and_withdrawals_retrieve_action_task_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :return: The deposits_and_withdrawals_retrieve_action_task_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: object
        """
        return self._deposits_and_withdrawals_retrieve_action_task_record

    @deposits_and_withdrawals_retrieve_action_task_record.setter
    def deposits_and_withdrawals_retrieve_action_task_record(self, deposits_and_withdrawals_retrieve_action_task_record):
        """Sets the deposits_and_withdrawals_retrieve_action_task_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :param deposits_and_withdrawals_retrieve_action_task_record: The deposits_and_withdrawals_retrieve_action_task_record of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_retrieve_action_task_record: object
        """

        self._deposits_and_withdrawals_retrieve_action_task_record = deposits_and_withdrawals_retrieve_action_task_record

    @property
    def deposits_and_withdrawals_retrieve_action_response(self):
        """Gets the deposits_and_withdrawals_retrieve_action_response of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :return: The deposits_and_withdrawals_retrieve_action_response of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: str
        """
        return self._deposits_and_withdrawals_retrieve_action_response

    @deposits_and_withdrawals_retrieve_action_response.setter
    def deposits_and_withdrawals_retrieve_action_response(self, deposits_and_withdrawals_retrieve_action_response):
        """Sets the deposits_and_withdrawals_retrieve_action_response of this BQDepositsAndWithdrawalsRetrieveOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :param deposits_and_withdrawals_retrieve_action_response: The deposits_and_withdrawals_retrieve_action_response of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_retrieve_action_response: str
        """

        self._deposits_and_withdrawals_retrieve_action_response = deposits_and_withdrawals_retrieve_action_response

    @property
    def deposits_and_withdrawals_instance_report(self):
        """Gets the deposits_and_withdrawals_instance_report of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :return: The deposits_and_withdrawals_instance_report of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceReport
        """
        return self._deposits_and_withdrawals_instance_report

    @deposits_and_withdrawals_instance_report.setter
    def deposits_and_withdrawals_instance_report(self, deposits_and_withdrawals_instance_report):
        """Sets the deposits_and_withdrawals_instance_report of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :param deposits_and_withdrawals_instance_report: The deposits_and_withdrawals_instance_report of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_instance_report: InlineResponse20017DepositsAndWithdrawalsInstanceReport
        """

        self._deposits_and_withdrawals_instance_report = deposits_and_withdrawals_instance_report

    @property
    def deposits_and_withdrawals_instance_analysis(self):
        """Gets the deposits_and_withdrawals_instance_analysis of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :return: The deposits_and_withdrawals_instance_analysis of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
        """
        return self._deposits_and_withdrawals_instance_analysis

    @deposits_and_withdrawals_instance_analysis.setter
    def deposits_and_withdrawals_instance_analysis(self, deposits_and_withdrawals_instance_analysis):
        """Sets the deposits_and_withdrawals_instance_analysis of this BQDepositsAndWithdrawalsRetrieveOutputModel.


        :param deposits_and_withdrawals_instance_analysis: The deposits_and_withdrawals_instance_analysis of this BQDepositsAndWithdrawalsRetrieveOutputModel.
        :type deposits_and_withdrawals_instance_analysis: InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
        """

        self._deposits_and_withdrawals_instance_analysis = deposits_and_withdrawals_instance_analysis