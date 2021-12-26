# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, activity_analysis_reference=None, activity_analysis_result=None, activity_analysis_report_type=None, activity_analysis_report=None):  # noqa: E501
        """InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis - a model defined in OpenAPI

        :param activity_analysis_reference: The activity_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.  # noqa: E501
        :type activity_analysis_reference: str
        :param activity_analysis_result: The activity_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.  # noqa: E501
        :type activity_analysis_result: str
        :param activity_analysis_report_type: The activity_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.  # noqa: E501
        :type activity_analysis_report_type: str
        :param activity_analysis_report: The activity_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.  # noqa: E501
        :type activity_analysis_report: object
        """
        self.openapi_types = {
            'activity_analysis_reference': str,
            'activity_analysis_result': str,
            'activity_analysis_report_type': str,
            'activity_analysis_report': object
        }

        self.attribute_map = {
            'activity_analysis_reference': 'activityAnalysisReference',
            'activity_analysis_result': 'activityAnalysisResult',
            'activity_analysis_report_type': 'activityAnalysisReportType',
            'activity_analysis_report': 'activityAnalysisReport'
        }

        self._activity_analysis_reference = activity_analysis_reference
        self._activity_analysis_result = activity_analysis_result
        self._activity_analysis_report_type = activity_analysis_report_type
        self._activity_analysis_report = activity_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2_serviceDomainRetrieveActionRecord_serviceDomainActivityAnalysis of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.  # noqa: E501
        :rtype: InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def activity_analysis_reference(self):
        """Gets the activity_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the internal activity analysis view maintained by the service center   # noqa: E501

        :return: The activity_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :rtype: str
        """
        return self._activity_analysis_reference

    @activity_analysis_reference.setter
    def activity_analysis_reference(self, activity_analysis_reference):
        """Sets the activity_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the internal activity analysis view maintained by the service center   # noqa: E501

        :param activity_analysis_reference: The activity_analysis_reference of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :type activity_analysis_reference: str
        """

        self._activity_analysis_reference = activity_analysis_reference

    @property
    def activity_analysis_result(self):
        """Gets the activity_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The results of the activity analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The activity_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :rtype: str
        """
        return self._activity_analysis_result

    @activity_analysis_result.setter
    def activity_analysis_result(self, activity_analysis_result):
        """Sets the activity_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The results of the activity analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :param activity_analysis_result: The activity_analysis_result of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :type activity_analysis_result: str
        """

        self._activity_analysis_result = activity_analysis_result

    @property
    def activity_analysis_report_type(self):
        """Gets the activity_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of activity analysis report available   # noqa: E501

        :return: The activity_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :rtype: str
        """
        return self._activity_analysis_report_type

    @activity_analysis_report_type.setter
    def activity_analysis_report_type(self, activity_analysis_report_type):
        """Sets the activity_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of activity analysis report available   # noqa: E501

        :param activity_analysis_report_type: The activity_analysis_report_type of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :type activity_analysis_report_type: str
        """

        self._activity_analysis_report_type = activity_analysis_report_type

    @property
    def activity_analysis_report(self):
        """Gets the activity_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The activity analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The activity_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :rtype: object
        """
        return self._activity_analysis_report

    @activity_analysis_report.setter
    def activity_analysis_report(self, activity_analysis_report):
        """Sets the activity_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The activity analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param activity_analysis_report: The activity_analysis_report of this InlineResponse2002ServiceDomainRetrieveActionRecordServiceDomainActivityAnalysis.
        :type activity_analysis_report: object
        """

        self._activity_analysis_report = activity_analysis_report
