# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_instance_analysis_reference=None):  # noqa: E501
        """BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1 - a model defined in OpenAPI

        :param issued_device_instance_analysis_reference: The issued_device_instance_analysis_reference of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.  # noqa: E501
        :type issued_device_instance_analysis_reference: str
        """
        self.openapi_types = {
            'issued_device_instance_analysis_reference': str
        }

        self.attribute_map = {
            'issued_device_instance_analysis_reference': 'issuedDeviceInstanceAnalysisReference'
        }

        self._issued_device_instance_analysis_reference = issued_device_instance_analysis_reference

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceRetrieveInputModel_issuedDeviceInstanceAnalysis_1 of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.  # noqa: E501
        :rtype: BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_instance_analysis_reference(self):
        """Gets the issued_device_instance_analysis_reference of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance analysis view   # noqa: E501

        :return: The issued_device_instance_analysis_reference of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.
        :rtype: str
        """
        return self._issued_device_instance_analysis_reference

    @issued_device_instance_analysis_reference.setter
    def issued_device_instance_analysis_reference(self, issued_device_instance_analysis_reference):
        """Sets the issued_device_instance_analysis_reference of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance analysis view   # noqa: E501

        :param issued_device_instance_analysis_reference: The issued_device_instance_analysis_reference of this BQIssuedDeviceRetrieveInputModelIssuedDeviceInstanceAnalysis1.
        :type issued_device_instance_analysis_reference: str
        """

        self._issued_device_instance_analysis_reference = issued_device_instance_analysis_reference
