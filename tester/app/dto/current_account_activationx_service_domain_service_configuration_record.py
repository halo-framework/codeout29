# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_activationx_service_domain_service_configuration_record_service_domain_service_configuration_setup import CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
from tester import util

from tester.app.dto.current_account_activationx_service_domain_service_configuration_record_service_domain_service_configuration_setup import CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup  # noqa: E501



class CurrentAccountActivationxServiceDomainServiceConfigurationRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_configuration_setting_reference=None, service_domain_service_configuration_setting_type=None, service_domain_service_configuration_setup=None):  # noqa: E501
        """CurrentAccountActivationxServiceDomainServiceConfigurationRecord - a model defined in OpenAPI

        :param service_domain_service_configuration_setting_reference: The service_domain_service_configuration_setting_reference of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_configuration_setting_reference: str
        :param service_domain_service_configuration_setting_type: The service_domain_service_configuration_setting_type of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_configuration_setting_type: str
        :param service_domain_service_configuration_setup: The service_domain_service_configuration_setup of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_configuration_setup: CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        """
        self.openapi_types = {
            'service_domain_service_configuration_setting_reference': str,
            'service_domain_service_configuration_setting_type': str,
            'service_domain_service_configuration_setup': CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        }

        self.attribute_map = {
            'service_domain_service_configuration_setting_reference': 'serviceDomainServiceConfigurationSettingReference',
            'service_domain_service_configuration_setting_type': 'serviceDomainServiceConfigurationSettingType',
            'service_domain_service_configuration_setup': 'serviceDomainServiceConfigurationSetup'
        }

        self._service_domain_service_configuration_setting_reference = service_domain_service_configuration_setting_reference
        self._service_domain_service_configuration_setting_type = service_domain_service_configuration_setting_type
        self._service_domain_service_configuration_setup = service_domain_service_configuration_setup

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountActivationxServiceDomainServiceConfigurationRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account_activationx_serviceDomainServiceConfigurationRecord of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.  # noqa: E501
        :rtype: CurrentAccountActivationxServiceDomainServiceConfigurationRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_configuration_setting_reference(self):
        """Gets the service_domain_service_configuration_setting_reference of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Refers to the service configuration parameter for the service   # noqa: E501

        :return: The service_domain_service_configuration_setting_reference of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :rtype: str
        """
        return self._service_domain_service_configuration_setting_reference

    @service_domain_service_configuration_setting_reference.setter
    def service_domain_service_configuration_setting_reference(self, service_domain_service_configuration_setting_reference):
        """Sets the service_domain_service_configuration_setting_reference of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Refers to the service configuration parameter for the service   # noqa: E501

        :param service_domain_service_configuration_setting_reference: The service_domain_service_configuration_setting_reference of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :type service_domain_service_configuration_setting_reference: str
        """

        self._service_domain_service_configuration_setting_reference = service_domain_service_configuration_setting_reference

    @property
    def service_domain_service_configuration_setting_type(self):
        """Gets the service_domain_service_configuration_setting_type of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of service configuration parameter   # noqa: E501

        :return: The service_domain_service_configuration_setting_type of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :rtype: str
        """
        return self._service_domain_service_configuration_setting_type

    @service_domain_service_configuration_setting_type.setter
    def service_domain_service_configuration_setting_type(self, service_domain_service_configuration_setting_type):
        """Sets the service_domain_service_configuration_setting_type of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of service configuration parameter   # noqa: E501

        :param service_domain_service_configuration_setting_type: The service_domain_service_configuration_setting_type of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :type service_domain_service_configuration_setting_type: str
        """

        self._service_domain_service_configuration_setting_type = service_domain_service_configuration_setting_type

    @property
    def service_domain_service_configuration_setup(self):
        """Gets the service_domain_service_configuration_setup of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.


        :return: The service_domain_service_configuration_setup of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :rtype: CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        """
        return self._service_domain_service_configuration_setup

    @service_domain_service_configuration_setup.setter
    def service_domain_service_configuration_setup(self, service_domain_service_configuration_setup):
        """Sets the service_domain_service_configuration_setup of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.


        :param service_domain_service_configuration_setup: The service_domain_service_configuration_setup of this CurrentAccountActivationxServiceDomainServiceConfigurationRecord.
        :type service_domain_service_configuration_setup: CurrentAccountActivationxServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        """

        self._service_domain_service_configuration_setup = service_domain_service_configuration_setup