# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, control_record_portfolio_analysis_reference=None, control_record_portfolio_analysis_result=None, control_record_portfolio_analysis_report_type=None, control_record_analysis_report=None):  # noqa: E501
        """InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis - a model defined in OpenAPI

        :param control_record_portfolio_analysis_reference: The control_record_portfolio_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.  # noqa: E501
        :type control_record_portfolio_analysis_reference: str
        :param control_record_portfolio_analysis_result: The control_record_portfolio_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.  # noqa: E501
        :type control_record_portfolio_analysis_result: str
        :param control_record_portfolio_analysis_report_type: The control_record_portfolio_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.  # noqa: E501
        :type control_record_portfolio_analysis_report_type: str
        :param control_record_analysis_report: The control_record_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.  # noqa: E501
        :type control_record_analysis_report: object
        """
        self.openapi_types = {
            'control_record_portfolio_analysis_reference': str,
            'control_record_portfolio_analysis_result': str,
            'control_record_portfolio_analysis_report_type': str,
            'control_record_analysis_report': object
        }

        self.attribute_map = {
            'control_record_portfolio_analysis_reference': 'controlRecordPortfolioAnalysisReference',
            'control_record_portfolio_analysis_result': 'controlRecordPortfolioAnalysisResult',
            'control_record_portfolio_analysis_report_type': 'controlRecordPortfolioAnalysisReportType',
            'control_record_analysis_report': 'controlRecordAnalysisReport'
        }

        self._control_record_portfolio_analysis_reference = control_record_portfolio_analysis_reference
        self._control_record_portfolio_analysis_result = control_record_portfolio_analysis_result
        self._control_record_portfolio_analysis_report_type = control_record_portfolio_analysis_report_type
        self._control_record_analysis_report = control_record_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2_serviceDomainRetrieveActionRecord_controlRecordPortfolioAnalysis of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.  # noqa: E501
        :rtype: InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def control_record_portfolio_analysis_reference(self):
        """Gets the control_record_portfolio_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record portfolio analysis view maintained by the service center   # noqa: E501

        :return: The control_record_portfolio_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :rtype: str
        """
        return self._control_record_portfolio_analysis_reference

    @control_record_portfolio_analysis_reference.setter
    def control_record_portfolio_analysis_reference(self, control_record_portfolio_analysis_reference):
        """Sets the control_record_portfolio_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record portfolio analysis view maintained by the service center   # noqa: E501

        :param control_record_portfolio_analysis_reference: The control_record_portfolio_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :type control_record_portfolio_analysis_reference: str
        """

        self._control_record_portfolio_analysis_reference = control_record_portfolio_analysis_reference

    @property
    def control_record_portfolio_analysis_result(self):
        """Gets the control_record_portfolio_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The results of the portfolio analysis that can be on-going, periodic and actual and projected (can be unstructured data)   # noqa: E501

        :return: The control_record_portfolio_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :rtype: str
        """
        return self._control_record_portfolio_analysis_result

    @control_record_portfolio_analysis_result.setter
    def control_record_portfolio_analysis_result(self, control_record_portfolio_analysis_result):
        """Sets the control_record_portfolio_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The results of the portfolio analysis that can be on-going, periodic and actual and projected (can be unstructured data)   # noqa: E501

        :param control_record_portfolio_analysis_result: The control_record_portfolio_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :type control_record_portfolio_analysis_result: str
        """

        self._control_record_portfolio_analysis_result = control_record_portfolio_analysis_result

    @property
    def control_record_portfolio_analysis_report_type(self):
        """Gets the control_record_portfolio_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external portfolio analysis report available   # noqa: E501

        :return: The control_record_portfolio_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :rtype: str
        """
        return self._control_record_portfolio_analysis_report_type

    @control_record_portfolio_analysis_report_type.setter
    def control_record_portfolio_analysis_report_type(self, control_record_portfolio_analysis_report_type):
        """Sets the control_record_portfolio_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external portfolio analysis report available   # noqa: E501

        :param control_record_portfolio_analysis_report_type: The control_record_portfolio_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :type control_record_portfolio_analysis_report_type: str
        """

        self._control_record_portfolio_analysis_report_type = control_record_portfolio_analysis_report_type

    @property
    def control_record_analysis_report(self):
        """Gets the control_record_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The control_record_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :rtype: object
        """
        return self._control_record_analysis_report

    @control_record_analysis_report.setter
    def control_record_analysis_report(self, control_record_analysis_report):
        """Sets the control_record_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param control_record_analysis_report: The control_record_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordControlRecordPortfolioAnalysis.
        :type control_record_analysis_report: object
        """

        self._control_record_analysis_report = control_record_analysis_report
