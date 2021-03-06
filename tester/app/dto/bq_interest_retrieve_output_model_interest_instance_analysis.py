# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQInterestRetrieveOutputModelInterestInstanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interest_instance_analysis_record=None, interest_instance_analysis_report_type=None, interest_instance_analysis_parameters=None, interest_instance_analysis_report=None):  # noqa: E501
        """BQInterestRetrieveOutputModelInterestInstanceAnalysis - a model defined in OpenAPI

        :param interest_instance_analysis_record: The interest_instance_analysis_record of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.  # noqa: E501
        :type interest_instance_analysis_record: object
        :param interest_instance_analysis_report_type: The interest_instance_analysis_report_type of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.  # noqa: E501
        :type interest_instance_analysis_report_type: str
        :param interest_instance_analysis_parameters: The interest_instance_analysis_parameters of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.  # noqa: E501
        :type interest_instance_analysis_parameters: str
        :param interest_instance_analysis_report: The interest_instance_analysis_report of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.  # noqa: E501
        :type interest_instance_analysis_report: object
        """
        self.openapi_types = {
            'interest_instance_analysis_record': object,
            'interest_instance_analysis_report_type': str,
            'interest_instance_analysis_parameters': str,
            'interest_instance_analysis_report': object
        }

        self.attribute_map = {
            'interest_instance_analysis_record': 'interestInstanceAnalysisRecord',
            'interest_instance_analysis_report_type': 'interestInstanceAnalysisReportType',
            'interest_instance_analysis_parameters': 'interestInstanceAnalysisParameters',
            'interest_instance_analysis_report': 'interestInstanceAnalysisReport'
        }

        self._interest_instance_analysis_record = interest_instance_analysis_record
        self._interest_instance_analysis_report_type = interest_instance_analysis_report_type
        self._interest_instance_analysis_parameters = interest_instance_analysis_parameters
        self._interest_instance_analysis_report = interest_instance_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'BQInterestRetrieveOutputModelInterestInstanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQInterestRetrieveOutputModel_interestInstanceAnalysis of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.  # noqa: E501
        :rtype: BQInterestRetrieveOutputModelInterestInstanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interest_instance_analysis_record(self):
        """Gets the interest_instance_analysis_record of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The interest_instance_analysis_record of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :rtype: object
        """
        return self._interest_instance_analysis_record

    @interest_instance_analysis_record.setter
    def interest_instance_analysis_record(self, interest_instance_analysis_record):
        """Sets the interest_instance_analysis_record of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :param interest_instance_analysis_record: The interest_instance_analysis_record of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :type interest_instance_analysis_record: object
        """

        self._interest_instance_analysis_record = interest_instance_analysis_record

    @property
    def interest_instance_analysis_report_type(self):
        """Gets the interest_instance_analysis_report_type of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :return: The interest_instance_analysis_report_type of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :rtype: str
        """
        return self._interest_instance_analysis_report_type

    @interest_instance_analysis_report_type.setter
    def interest_instance_analysis_report_type(self, interest_instance_analysis_report_type):
        """Sets the interest_instance_analysis_report_type of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :param interest_instance_analysis_report_type: The interest_instance_analysis_report_type of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :type interest_instance_analysis_report_type: str
        """

        self._interest_instance_analysis_report_type = interest_instance_analysis_report_type

    @property
    def interest_instance_analysis_parameters(self):
        """Gets the interest_instance_analysis_parameters of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :return: The interest_instance_analysis_parameters of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :rtype: str
        """
        return self._interest_instance_analysis_parameters

    @interest_instance_analysis_parameters.setter
    def interest_instance_analysis_parameters(self, interest_instance_analysis_parameters):
        """Sets the interest_instance_analysis_parameters of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :param interest_instance_analysis_parameters: The interest_instance_analysis_parameters of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :type interest_instance_analysis_parameters: str
        """

        self._interest_instance_analysis_parameters = interest_instance_analysis_parameters

    @property
    def interest_instance_analysis_report(self):
        """Gets the interest_instance_analysis_report of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The interest_instance_analysis_report of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :rtype: object
        """
        return self._interest_instance_analysis_report

    @interest_instance_analysis_report.setter
    def interest_instance_analysis_report(self, interest_instance_analysis_report):
        """Sets the interest_instance_analysis_report of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param interest_instance_analysis_report: The interest_instance_analysis_report of this BQInterestRetrieveOutputModelInterestInstanceAnalysis.
        :type interest_instance_analysis_report: object
        """

        self._interest_instance_analysis_report = interest_instance_analysis_report
