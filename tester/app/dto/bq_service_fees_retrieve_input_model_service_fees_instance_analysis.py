# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_fees_instance_analysis_reference=None):  # noqa: E501
        """BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis - a model defined in OpenAPI

        :param service_fees_instance_analysis_reference: The service_fees_instance_analysis_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.  # noqa: E501
        :type service_fees_instance_analysis_reference: str
        """
        self.openapi_types = {
            'service_fees_instance_analysis_reference': str
        }

        self.attribute_map = {
            'service_fees_instance_analysis_reference': 'serviceFeesInstanceAnalysisReference'
        }

        self._service_fees_instance_analysis_reference = service_fees_instance_analysis_reference

    @classmethod
    def from_dict(cls, dikt) -> 'BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQServiceFeesRetrieveInputModel_serviceFeesInstanceAnalysis of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.  # noqa: E501
        :rtype: BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_fees_instance_analysis_reference(self):
        """Gets the service_fees_instance_analysis_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance analysis view   # noqa: E501

        :return: The service_fees_instance_analysis_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.
        :rtype: str
        """
        return self._service_fees_instance_analysis_reference

    @service_fees_instance_analysis_reference.setter
    def service_fees_instance_analysis_reference(self, service_fees_instance_analysis_reference):
        """Sets the service_fees_instance_analysis_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance analysis view   # noqa: E501

        :param service_fees_instance_analysis_reference: The service_fees_instance_analysis_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceAnalysis.
        :type service_fees_instance_analysis_reference: str
        """

        self._service_fees_instance_analysis_reference = service_fees_instance_analysis_reference
