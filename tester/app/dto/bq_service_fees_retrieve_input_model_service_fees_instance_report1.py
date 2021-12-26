# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_fees_instance_report_reference=None):  # noqa: E501
        """BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1 - a model defined in OpenAPI

        :param service_fees_instance_report_reference: The service_fees_instance_report_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.  # noqa: E501
        :type service_fees_instance_report_reference: str
        """
        self.openapi_types = {
            'service_fees_instance_report_reference': str
        }

        self.attribute_map = {
            'service_fees_instance_report_reference': 'serviceFeesInstanceReportReference'
        }

        self._service_fees_instance_report_reference = service_fees_instance_report_reference

    @classmethod
    def from_dict(cls, dikt) -> 'BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQServiceFeesRetrieveInputModel_serviceFeesInstanceReport_1 of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.  # noqa: E501
        :rtype: BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_fees_instance_report_reference(self):
        """Gets the service_fees_instance_report_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance report   # noqa: E501

        :return: The service_fees_instance_report_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.
        :rtype: str
        """
        return self._service_fees_instance_report_reference

    @service_fees_instance_report_reference.setter
    def service_fees_instance_report_reference(self, service_fees_instance_report_reference):
        """Sets the service_fees_instance_report_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance report   # noqa: E501

        :param service_fees_instance_report_reference: The service_fees_instance_report_reference of this BQServiceFeesRetrieveInputModelServiceFeesInstanceReport1.
        :type service_fees_instance_report_reference: str
        """

        self._service_fees_instance_report_reference = service_fees_instance_report_reference