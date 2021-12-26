# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse20021PaymentsInstanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payments_instance_analysis_record=None, payments_instance_analysis_report_type=None, payments_instance_analysis_parameters=None, payments_instance_analysis_report=None):  # noqa: E501
        """InlineResponse20021PaymentsInstanceAnalysis - a model defined in OpenAPI

        :param payments_instance_analysis_record: The payments_instance_analysis_record of this InlineResponse20021PaymentsInstanceAnalysis.  # noqa: E501
        :type payments_instance_analysis_record: object
        :param payments_instance_analysis_report_type: The payments_instance_analysis_report_type of this InlineResponse20021PaymentsInstanceAnalysis.  # noqa: E501
        :type payments_instance_analysis_report_type: str
        :param payments_instance_analysis_parameters: The payments_instance_analysis_parameters of this InlineResponse20021PaymentsInstanceAnalysis.  # noqa: E501
        :type payments_instance_analysis_parameters: str
        :param payments_instance_analysis_report: The payments_instance_analysis_report of this InlineResponse20021PaymentsInstanceAnalysis.  # noqa: E501
        :type payments_instance_analysis_report: object
        """
        self.openapi_types = {
            'payments_instance_analysis_record': object,
            'payments_instance_analysis_report_type': str,
            'payments_instance_analysis_parameters': str,
            'payments_instance_analysis_report': object
        }

        self.attribute_map = {
            'payments_instance_analysis_record': 'paymentsInstanceAnalysisRecord',
            'payments_instance_analysis_report_type': 'paymentsInstanceAnalysisReportType',
            'payments_instance_analysis_parameters': 'paymentsInstanceAnalysisParameters',
            'payments_instance_analysis_report': 'paymentsInstanceAnalysisReport'
        }

        self._payments_instance_analysis_record = payments_instance_analysis_record
        self._payments_instance_analysis_report_type = payments_instance_analysis_report_type
        self._payments_instance_analysis_parameters = payments_instance_analysis_parameters
        self._payments_instance_analysis_report = payments_instance_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20021PaymentsInstanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_21_paymentsInstanceAnalysis of this InlineResponse20021PaymentsInstanceAnalysis.  # noqa: E501
        :rtype: InlineResponse20021PaymentsInstanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payments_instance_analysis_record(self):
        """Gets the payments_instance_analysis_record of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The payments_instance_analysis_record of this InlineResponse20021PaymentsInstanceAnalysis.
        :rtype: object
        """
        return self._payments_instance_analysis_record

    @payments_instance_analysis_record.setter
    def payments_instance_analysis_record(self, payments_instance_analysis_record):
        """Sets the payments_instance_analysis_record of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :param payments_instance_analysis_record: The payments_instance_analysis_record of this InlineResponse20021PaymentsInstanceAnalysis.
        :type payments_instance_analysis_record: object
        """

        self._payments_instance_analysis_record = payments_instance_analysis_record

    @property
    def payments_instance_analysis_report_type(self):
        """Gets the payments_instance_analysis_report_type of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :return: The payments_instance_analysis_report_type of this InlineResponse20021PaymentsInstanceAnalysis.
        :rtype: str
        """
        return self._payments_instance_analysis_report_type

    @payments_instance_analysis_report_type.setter
    def payments_instance_analysis_report_type(self, payments_instance_analysis_report_type):
        """Sets the payments_instance_analysis_report_type of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :param payments_instance_analysis_report_type: The payments_instance_analysis_report_type of this InlineResponse20021PaymentsInstanceAnalysis.
        :type payments_instance_analysis_report_type: str
        """

        self._payments_instance_analysis_report_type = payments_instance_analysis_report_type

    @property
    def payments_instance_analysis_parameters(self):
        """Gets the payments_instance_analysis_parameters of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :return: The payments_instance_analysis_parameters of this InlineResponse20021PaymentsInstanceAnalysis.
        :rtype: str
        """
        return self._payments_instance_analysis_parameters

    @payments_instance_analysis_parameters.setter
    def payments_instance_analysis_parameters(self, payments_instance_analysis_parameters):
        """Sets the payments_instance_analysis_parameters of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :param payments_instance_analysis_parameters: The payments_instance_analysis_parameters of this InlineResponse20021PaymentsInstanceAnalysis.
        :type payments_instance_analysis_parameters: str
        """

        self._payments_instance_analysis_parameters = payments_instance_analysis_parameters

    @property
    def payments_instance_analysis_report(self):
        """Gets the payments_instance_analysis_report of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The payments_instance_analysis_report of this InlineResponse20021PaymentsInstanceAnalysis.
        :rtype: object
        """
        return self._payments_instance_analysis_report

    @payments_instance_analysis_report.setter
    def payments_instance_analysis_report(self, payments_instance_analysis_report):
        """Sets the payments_instance_analysis_report of this InlineResponse20021PaymentsInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param payments_instance_analysis_report: The payments_instance_analysis_report of this InlineResponse20021PaymentsInstanceAnalysis.
        :type payments_instance_analysis_report: object
        """

        self._payments_instance_analysis_report = payments_instance_analysis_report