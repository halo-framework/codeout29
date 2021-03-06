# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2002_service_domain_offered_service_service_domain_service_record_service_domain_service_policiesand_guidelines import InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines
from tester import util

from tester.app.dto.inline_response2002_service_domain_offered_service_service_domain_service_record_service_domain_service_policiesand_guidelines import InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines  # noqa: E501



class InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_type=None, service_domain_service_version=None, service_domain_service_description=None, service_domain_service_policiesand_guidelines=None, service_domain_service_schedule=None):  # noqa: E501
        """InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord - a model defined in OpenAPI

        :param service_domain_service_type: The service_domain_service_type of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :type service_domain_service_type: str
        :param service_domain_service_version: The service_domain_service_version of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :type service_domain_service_version: str
        :param service_domain_service_description: The service_domain_service_description of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :type service_domain_service_description: str
        :param service_domain_service_policiesand_guidelines: The service_domain_service_policiesand_guidelines of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :type service_domain_service_policiesand_guidelines: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines
        :param service_domain_service_schedule: The service_domain_service_schedule of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :type service_domain_service_schedule: str
        """
        self.openapi_types = {
            'service_domain_service_type': str,
            'service_domain_service_version': str,
            'service_domain_service_description': str,
            'service_domain_service_policiesand_guidelines': InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines,
            'service_domain_service_schedule': str
        }

        self.attribute_map = {
            'service_domain_service_type': 'serviceDomainServiceType',
            'service_domain_service_version': 'serviceDomainServiceVersion',
            'service_domain_service_description': 'serviceDomainServiceDescription',
            'service_domain_service_policiesand_guidelines': 'serviceDomainServicePoliciesandGuidelines',
            'service_domain_service_schedule': 'serviceDomainServiceSchedule'
        }

        self._service_domain_service_type = service_domain_service_type
        self._service_domain_service_version = service_domain_service_version
        self._service_domain_service_description = service_domain_service_description
        self._service_domain_service_policiesand_guidelines = service_domain_service_policiesand_guidelines
        self._service_domain_service_schedule = service_domain_service_schedule

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2_serviceDomainOfferedService_serviceDomainServiceRecord of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.  # noqa: E501
        :rtype: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_type(self):
        """Gets the service_domain_service_type of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Refers to the different types of services offered   # noqa: E501

        :return: The service_domain_service_type of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :rtype: str
        """
        return self._service_domain_service_type

    @service_domain_service_type.setter
    def service_domain_service_type(self, service_domain_service_type):
        """Sets the service_domain_service_type of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Refers to the different types of services offered   # noqa: E501

        :param service_domain_service_type: The service_domain_service_type of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :type service_domain_service_type: str
        """

        self._service_domain_service_type = service_domain_service_type

    @property
    def service_domain_service_version(self):
        """Gets the service_domain_service_version of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The version details of the service when appropriate   # noqa: E501

        :return: The service_domain_service_version of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :rtype: str
        """
        return self._service_domain_service_version

    @service_domain_service_version.setter
    def service_domain_service_version(self, service_domain_service_version):
        """Sets the service_domain_service_version of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The version details of the service when appropriate   # noqa: E501

        :param service_domain_service_version: The service_domain_service_version of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :type service_domain_service_version: str
        """

        self._service_domain_service_version = service_domain_service_version

    @property
    def service_domain_service_description(self):
        """Gets the service_domain_service_description of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the offered service    # noqa: E501

        :return: The service_domain_service_description of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :rtype: str
        """
        return self._service_domain_service_description

    @service_domain_service_description.setter
    def service_domain_service_description(self, service_domain_service_description):
        """Sets the service_domain_service_description of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the offered service    # noqa: E501

        :param service_domain_service_description: The service_domain_service_description of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :type service_domain_service_description: str
        """

        self._service_domain_service_description = service_domain_service_description

    @property
    def service_domain_service_policiesand_guidelines(self):
        """Gets the service_domain_service_policiesand_guidelines of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.


        :return: The service_domain_service_policiesand_guidelines of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :rtype: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines
        """
        return self._service_domain_service_policiesand_guidelines

    @service_domain_service_policiesand_guidelines.setter
    def service_domain_service_policiesand_guidelines(self, service_domain_service_policiesand_guidelines):
        """Sets the service_domain_service_policiesand_guidelines of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.


        :param service_domain_service_policiesand_guidelines: The service_domain_service_policiesand_guidelines of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :type service_domain_service_policiesand_guidelines: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecordServiceDomainServicePoliciesandGuidelines
        """

        self._service_domain_service_policiesand_guidelines = service_domain_service_policiesand_guidelines

    @property
    def service_domain_service_schedule(self):
        """Gets the service_domain_service_schedule of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Schedule defining when the accessed service is available   # noqa: E501

        :return: The service_domain_service_schedule of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :rtype: str
        """
        return self._service_domain_service_schedule

    @service_domain_service_schedule.setter
    def service_domain_service_schedule(self, service_domain_service_schedule):
        """Sets the service_domain_service_schedule of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Schedule defining when the accessed service is available   # noqa: E501

        :param service_domain_service_schedule: The service_domain_service_schedule of this InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord.
        :type service_domain_service_schedule: str
        """

        self._service_domain_service_schedule = service_domain_service_schedule
