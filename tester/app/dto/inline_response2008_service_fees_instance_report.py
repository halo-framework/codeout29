# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2008ServiceFeesInstanceReport(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_fees_instance_report_record=None, service_fees_instance_report_type=None, service_fees_instance_report_parameters=None, service_fees_instance_report=None):  # noqa: E501
        """InlineResponse2008ServiceFeesInstanceReport - a model defined in OpenAPI

        :param service_fees_instance_report_record: The service_fees_instance_report_record of this InlineResponse2008ServiceFeesInstanceReport.  # noqa: E501
        :type service_fees_instance_report_record: object
        :param service_fees_instance_report_type: The service_fees_instance_report_type of this InlineResponse2008ServiceFeesInstanceReport.  # noqa: E501
        :type service_fees_instance_report_type: str
        :param service_fees_instance_report_parameters: The service_fees_instance_report_parameters of this InlineResponse2008ServiceFeesInstanceReport.  # noqa: E501
        :type service_fees_instance_report_parameters: str
        :param service_fees_instance_report: The service_fees_instance_report of this InlineResponse2008ServiceFeesInstanceReport.  # noqa: E501
        :type service_fees_instance_report: object
        """
        self.openapi_types = {
            'service_fees_instance_report_record': object,
            'service_fees_instance_report_type': str,
            'service_fees_instance_report_parameters': str,
            'service_fees_instance_report': object
        }

        self.attribute_map = {
            'service_fees_instance_report_record': 'serviceFeesInstanceReportRecord',
            'service_fees_instance_report_type': 'serviceFeesInstanceReportType',
            'service_fees_instance_report_parameters': 'serviceFeesInstanceReportParameters',
            'service_fees_instance_report': 'serviceFeesInstanceReport'
        }

        self._service_fees_instance_report_record = service_fees_instance_report_record
        self._service_fees_instance_report_type = service_fees_instance_report_type
        self._service_fees_instance_report_parameters = service_fees_instance_report_parameters
        self._service_fees_instance_report = service_fees_instance_report

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2008ServiceFeesInstanceReport':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8_serviceFeesInstanceReport of this InlineResponse2008ServiceFeesInstanceReport.  # noqa: E501
        :rtype: InlineResponse2008ServiceFeesInstanceReport
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_fees_instance_report_record(self):
        """Gets the service_fees_instance_report_record of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The input information used to assemble the report that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The service_fees_instance_report_record of this InlineResponse2008ServiceFeesInstanceReport.
        :rtype: object
        """
        return self._service_fees_instance_report_record

    @service_fees_instance_report_record.setter
    def service_fees_instance_report_record(self, service_fees_instance_report_record):
        """Sets the service_fees_instance_report_record of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The input information used to assemble the report that can be on-going, periodic and actual and projected   # noqa: E501

        :param service_fees_instance_report_record: The service_fees_instance_report_record of this InlineResponse2008ServiceFeesInstanceReport.
        :type service_fees_instance_report_record: object
        """

        self._service_fees_instance_report_record = service_fees_instance_report_record

    @property
    def service_fees_instance_report_type(self):
        """Gets the service_fees_instance_report_type of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external report available   # noqa: E501

        :return: The service_fees_instance_report_type of this InlineResponse2008ServiceFeesInstanceReport.
        :rtype: str
        """
        return self._service_fees_instance_report_type

    @service_fees_instance_report_type.setter
    def service_fees_instance_report_type(self, service_fees_instance_report_type):
        """Sets the service_fees_instance_report_type of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external report available   # noqa: E501

        :param service_fees_instance_report_type: The service_fees_instance_report_type of this InlineResponse2008ServiceFeesInstanceReport.
        :type service_fees_instance_report_type: str
        """

        self._service_fees_instance_report_type = service_fees_instance_report_type

    @property
    def service_fees_instance_report_parameters(self):
        """Gets the service_fees_instance_report_parameters of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the report (e.g. period, content type)   # noqa: E501

        :return: The service_fees_instance_report_parameters of this InlineResponse2008ServiceFeesInstanceReport.
        :rtype: str
        """
        return self._service_fees_instance_report_parameters

    @service_fees_instance_report_parameters.setter
    def service_fees_instance_report_parameters(self, service_fees_instance_report_parameters):
        """Sets the service_fees_instance_report_parameters of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the report (e.g. period, content type)   # noqa: E501

        :param service_fees_instance_report_parameters: The service_fees_instance_report_parameters of this InlineResponse2008ServiceFeesInstanceReport.
        :type service_fees_instance_report_parameters: str
        """

        self._service_fees_instance_report_parameters = service_fees_instance_report_parameters

    @property
    def service_fees_instance_report(self):
        """Gets the service_fees_instance_report of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The service_fees_instance_report of this InlineResponse2008ServiceFeesInstanceReport.
        :rtype: object
        """
        return self._service_fees_instance_report

    @service_fees_instance_report.setter
    def service_fees_instance_report(self, service_fees_instance_report):
        """Sets the service_fees_instance_report of this InlineResponse2008ServiceFeesInstanceReport.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external report in any suitable form including selection filters where appropriate   # noqa: E501

        :param service_fees_instance_report: The service_fees_instance_report of this InlineResponse2008ServiceFeesInstanceReport.
        :type service_fees_instance_report: object
        """

        self._service_fees_instance_report = service_fees_instance_report
