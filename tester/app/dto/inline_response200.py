# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response200_service_domain_service_configuration_record import InlineResponse200ServiceDomainServiceConfigurationRecord
from tester import util

from tester.app.dto.inline_response200_service_domain_service_configuration_record import InlineResponse200ServiceDomainServiceConfigurationRecord  # noqa: E501



class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_configuration_action_task_reference=None, service_domain_configuration_action_task_record=None, service_domain_service_configuration_record=None, service_domain_servicing_session_status=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param service_domain_configuration_action_task_reference: The service_domain_configuration_action_task_reference of this InlineResponse200.  # noqa: E501
        :type service_domain_configuration_action_task_reference: str
        :param service_domain_configuration_action_task_record: The service_domain_configuration_action_task_record of this InlineResponse200.  # noqa: E501
        :type service_domain_configuration_action_task_record: object
        :param service_domain_service_configuration_record: The service_domain_service_configuration_record of this InlineResponse200.  # noqa: E501
        :type service_domain_service_configuration_record: InlineResponse200ServiceDomainServiceConfigurationRecord
        :param service_domain_servicing_session_status: The service_domain_servicing_session_status of this InlineResponse200.  # noqa: E501
        :type service_domain_servicing_session_status: str
        """
        self.openapi_types = {
            'service_domain_configuration_action_task_reference': str,
            'service_domain_configuration_action_task_record': object,
            'service_domain_service_configuration_record': InlineResponse200ServiceDomainServiceConfigurationRecord,
            'service_domain_servicing_session_status': str
        }

        self.attribute_map = {
            'service_domain_configuration_action_task_reference': 'serviceDomainConfigurationActionTaskReference',
            'service_domain_configuration_action_task_record': 'serviceDomainConfigurationActionTaskRecord',
            'service_domain_service_configuration_record': 'serviceDomainServiceConfigurationRecord',
            'service_domain_servicing_session_status': 'serviceDomainServicingSessionStatus'
        }

        self._service_domain_configuration_action_task_reference = service_domain_configuration_action_task_reference
        self._service_domain_configuration_action_task_record = service_domain_configuration_action_task_record
        self._service_domain_service_configuration_record = service_domain_service_configuration_record
        self._service_domain_servicing_session_status = service_domain_servicing_session_status

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_configuration_action_task_reference(self):
        """Gets the service_domain_configuration_action_task_reference of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a service configuration service call   # noqa: E501

        :return: The service_domain_configuration_action_task_reference of this InlineResponse200.
        :rtype: str
        """
        return self._service_domain_configuration_action_task_reference

    @service_domain_configuration_action_task_reference.setter
    def service_domain_configuration_action_task_reference(self, service_domain_configuration_action_task_reference):
        """Sets the service_domain_configuration_action_task_reference of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a service configuration service call   # noqa: E501

        :param service_domain_configuration_action_task_reference: The service_domain_configuration_action_task_reference of this InlineResponse200.
        :type service_domain_configuration_action_task_reference: str
        """

        self._service_domain_configuration_action_task_reference = service_domain_configuration_action_task_reference

    @property
    def service_domain_configuration_action_task_record(self):
        """Gets the service_domain_configuration_action_task_record of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The configuration service call consolidated processing record   # noqa: E501

        :return: The service_domain_configuration_action_task_record of this InlineResponse200.
        :rtype: object
        """
        return self._service_domain_configuration_action_task_record

    @service_domain_configuration_action_task_record.setter
    def service_domain_configuration_action_task_record(self, service_domain_configuration_action_task_record):
        """Sets the service_domain_configuration_action_task_record of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The configuration service call consolidated processing record   # noqa: E501

        :param service_domain_configuration_action_task_record: The service_domain_configuration_action_task_record of this InlineResponse200.
        :type service_domain_configuration_action_task_record: object
        """

        self._service_domain_configuration_action_task_record = service_domain_configuration_action_task_record

    @property
    def service_domain_service_configuration_record(self):
        """Gets the service_domain_service_configuration_record of this InlineResponse200.


        :return: The service_domain_service_configuration_record of this InlineResponse200.
        :rtype: InlineResponse200ServiceDomainServiceConfigurationRecord
        """
        return self._service_domain_service_configuration_record

    @service_domain_service_configuration_record.setter
    def service_domain_service_configuration_record(self, service_domain_service_configuration_record):
        """Sets the service_domain_service_configuration_record of this InlineResponse200.


        :param service_domain_service_configuration_record: The service_domain_service_configuration_record of this InlineResponse200.
        :type service_domain_service_configuration_record: InlineResponse200ServiceDomainServiceConfigurationRecord
        """

        self._service_domain_service_configuration_record = service_domain_service_configuration_record

    @property
    def service_domain_servicing_session_status(self):
        """Gets the service_domain_servicing_session_status of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The current operating status of the overall servicing session   # noqa: E501

        :return: The service_domain_servicing_session_status of this InlineResponse200.
        :rtype: str
        """
        return self._service_domain_servicing_session_status

    @service_domain_servicing_session_status.setter
    def service_domain_servicing_session_status(self, service_domain_servicing_session_status):
        """Sets the service_domain_servicing_session_status of this InlineResponse200.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The current operating status of the overall servicing session   # noqa: E501

        :param service_domain_servicing_session_status: The service_domain_servicing_session_status of this InlineResponse200.
        :type service_domain_servicing_session_status: str
        """

        self._service_domain_servicing_session_status = service_domain_servicing_session_status
