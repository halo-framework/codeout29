# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, performance_analysis_reference=None):  # noqa: E501
        """SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis - a model defined in OpenAPI

        :param performance_analysis_reference: The performance_analysis_reference of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.  # noqa: E501
        :type performance_analysis_reference: str
        """
        self.openapi_types = {
            'performance_analysis_reference': str
        }

        self.attribute_map = {
            'performance_analysis_reference': 'performanceAnalysisReference'
        }

        self._performance_analysis_reference = performance_analysis_reference

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountRetrieveInputModel_serviceDomainRetrieveActionRecord_serviceDomainPerformanceAnalysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.  # noqa: E501
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def performance_analysis_reference(self):
        """Gets the performance_analysis_reference of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the internal performance analysis view maintained by the service center   # noqa: E501

        :return: The performance_analysis_reference of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.
        :rtype: str
        """
        return self._performance_analysis_reference

    @performance_analysis_reference.setter
    def performance_analysis_reference(self, performance_analysis_reference):
        """Sets the performance_analysis_reference of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the internal performance analysis view maintained by the service center   # noqa: E501

        :param performance_analysis_reference: The performance_analysis_reference of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecordServiceDomainPerformanceAnalysis.
        :type performance_analysis_reference: str
        """

        self._performance_analysis_reference = performance_analysis_reference