# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deposits_and_withdrawals_instance_analysis_record=None, deposits_and_withdrawals_instance_analysis_report_type=None, deposits_and_withdrawals_instance_analysis_parameters=None, deposits_and_withdrawals_instance_analysis_report=None):  # noqa: E501
        """InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis - a model defined in OpenAPI

        :param deposits_and_withdrawals_instance_analysis_record: The deposits_and_withdrawals_instance_analysis_record of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.  # noqa: E501
        :type deposits_and_withdrawals_instance_analysis_record: object
        :param deposits_and_withdrawals_instance_analysis_report_type: The deposits_and_withdrawals_instance_analysis_report_type of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.  # noqa: E501
        :type deposits_and_withdrawals_instance_analysis_report_type: str
        :param deposits_and_withdrawals_instance_analysis_parameters: The deposits_and_withdrawals_instance_analysis_parameters of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.  # noqa: E501
        :type deposits_and_withdrawals_instance_analysis_parameters: str
        :param deposits_and_withdrawals_instance_analysis_report: The deposits_and_withdrawals_instance_analysis_report of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.  # noqa: E501
        :type deposits_and_withdrawals_instance_analysis_report: object
        """
        self.openapi_types = {
            'deposits_and_withdrawals_instance_analysis_record': object,
            'deposits_and_withdrawals_instance_analysis_report_type': str,
            'deposits_and_withdrawals_instance_analysis_parameters': str,
            'deposits_and_withdrawals_instance_analysis_report': object
        }

        self.attribute_map = {
            'deposits_and_withdrawals_instance_analysis_record': 'depositsAndWithdrawalsInstanceAnalysisRecord',
            'deposits_and_withdrawals_instance_analysis_report_type': 'depositsAndWithdrawalsInstanceAnalysisReportType',
            'deposits_and_withdrawals_instance_analysis_parameters': 'depositsAndWithdrawalsInstanceAnalysisParameters',
            'deposits_and_withdrawals_instance_analysis_report': 'depositsAndWithdrawalsInstanceAnalysisReport'
        }

        self._deposits_and_withdrawals_instance_analysis_record = deposits_and_withdrawals_instance_analysis_record
        self._deposits_and_withdrawals_instance_analysis_report_type = deposits_and_withdrawals_instance_analysis_report_type
        self._deposits_and_withdrawals_instance_analysis_parameters = deposits_and_withdrawals_instance_analysis_parameters
        self._deposits_and_withdrawals_instance_analysis_report = deposits_and_withdrawals_instance_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_17_depositsAndWithdrawalsInstanceAnalysis of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.  # noqa: E501
        :rtype: InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deposits_and_withdrawals_instance_analysis_record(self):
        """Gets the deposits_and_withdrawals_instance_analysis_record of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The deposits_and_withdrawals_instance_analysis_record of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :rtype: object
        """
        return self._deposits_and_withdrawals_instance_analysis_record

    @deposits_and_withdrawals_instance_analysis_record.setter
    def deposits_and_withdrawals_instance_analysis_record(self, deposits_and_withdrawals_instance_analysis_record):
        """Sets the deposits_and_withdrawals_instance_analysis_record of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :param deposits_and_withdrawals_instance_analysis_record: The deposits_and_withdrawals_instance_analysis_record of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :type deposits_and_withdrawals_instance_analysis_record: object
        """

        self._deposits_and_withdrawals_instance_analysis_record = deposits_and_withdrawals_instance_analysis_record

    @property
    def deposits_and_withdrawals_instance_analysis_report_type(self):
        """Gets the deposits_and_withdrawals_instance_analysis_report_type of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :return: The deposits_and_withdrawals_instance_analysis_report_type of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :rtype: str
        """
        return self._deposits_and_withdrawals_instance_analysis_report_type

    @deposits_and_withdrawals_instance_analysis_report_type.setter
    def deposits_and_withdrawals_instance_analysis_report_type(self, deposits_and_withdrawals_instance_analysis_report_type):
        """Sets the deposits_and_withdrawals_instance_analysis_report_type of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :param deposits_and_withdrawals_instance_analysis_report_type: The deposits_and_withdrawals_instance_analysis_report_type of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :type deposits_and_withdrawals_instance_analysis_report_type: str
        """

        self._deposits_and_withdrawals_instance_analysis_report_type = deposits_and_withdrawals_instance_analysis_report_type

    @property
    def deposits_and_withdrawals_instance_analysis_parameters(self):
        """Gets the deposits_and_withdrawals_instance_analysis_parameters of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :return: The deposits_and_withdrawals_instance_analysis_parameters of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :rtype: str
        """
        return self._deposits_and_withdrawals_instance_analysis_parameters

    @deposits_and_withdrawals_instance_analysis_parameters.setter
    def deposits_and_withdrawals_instance_analysis_parameters(self, deposits_and_withdrawals_instance_analysis_parameters):
        """Sets the deposits_and_withdrawals_instance_analysis_parameters of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :param deposits_and_withdrawals_instance_analysis_parameters: The deposits_and_withdrawals_instance_analysis_parameters of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :type deposits_and_withdrawals_instance_analysis_parameters: str
        """

        self._deposits_and_withdrawals_instance_analysis_parameters = deposits_and_withdrawals_instance_analysis_parameters

    @property
    def deposits_and_withdrawals_instance_analysis_report(self):
        """Gets the deposits_and_withdrawals_instance_analysis_report of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The deposits_and_withdrawals_instance_analysis_report of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :rtype: object
        """
        return self._deposits_and_withdrawals_instance_analysis_report

    @deposits_and_withdrawals_instance_analysis_report.setter
    def deposits_and_withdrawals_instance_analysis_report(self, deposits_and_withdrawals_instance_analysis_report):
        """Sets the deposits_and_withdrawals_instance_analysis_report of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param deposits_and_withdrawals_instance_analysis_report: The deposits_and_withdrawals_instance_analysis_report of this InlineResponse20017DepositsAndWithdrawalsInstanceAnalysis.
        :type deposits_and_withdrawals_instance_analysis_report: object
        """

        self._deposits_and_withdrawals_instance_analysis_report = deposits_and_withdrawals_instance_analysis_report
