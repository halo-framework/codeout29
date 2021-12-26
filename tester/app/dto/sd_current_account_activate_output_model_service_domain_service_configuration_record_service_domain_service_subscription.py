# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_subscriber_reference=None, service_domain_service_subscriber_access_profile=None):  # noqa: E501
        """SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription - a model defined in OpenAPI

        :param service_domain_service_subscriber_reference: The service_domain_service_subscriber_reference of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.  # noqa: E501
        :type service_domain_service_subscriber_reference: str
        :param service_domain_service_subscriber_access_profile: The service_domain_service_subscriber_access_profile of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.  # noqa: E501
        :type service_domain_service_subscriber_access_profile: str
        """
        self.openapi_types = {
            'service_domain_service_subscriber_reference': str,
            'service_domain_service_subscriber_access_profile': str
        }

        self.attribute_map = {
            'service_domain_service_subscriber_reference': 'serviceDomainServiceSubscriberReference',
            'service_domain_service_subscriber_access_profile': 'serviceDomainServiceSubscriberAccessProfile'
        }

        self._service_domain_service_subscriber_reference = service_domain_service_subscriber_reference
        self._service_domain_service_subscriber_access_profile = service_domain_service_subscriber_access_profile

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountActivateOutputModel_serviceDomainServiceConfigurationRecord_serviceDomainServiceSubscription of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.  # noqa: E501
        :rtype: SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_subscriber_reference(self):
        """Gets the service_domain_service_subscriber_reference of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Maintains reference to allowed users or subscribers to the service which can be any known party   # noqa: E501

        :return: The service_domain_service_subscriber_reference of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.
        :rtype: str
        """
        return self._service_domain_service_subscriber_reference

    @service_domain_service_subscriber_reference.setter
    def service_domain_service_subscriber_reference(self, service_domain_service_subscriber_reference):
        """Sets the service_domain_service_subscriber_reference of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Maintains reference to allowed users or subscribers to the service which can be any known party   # noqa: E501

        :param service_domain_service_subscriber_reference: The service_domain_service_subscriber_reference of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.
        :type service_domain_service_subscriber_reference: str
        """

        self._service_domain_service_subscriber_reference = service_domain_service_subscriber_reference

    @property
    def service_domain_service_subscriber_access_profile(self):
        """Gets the service_domain_service_subscriber_access_profile of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The allowed service access for a user or subscriber to the service which can be any known party   # noqa: E501

        :return: The service_domain_service_subscriber_access_profile of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.
        :rtype: str
        """
        return self._service_domain_service_subscriber_access_profile

    @service_domain_service_subscriber_access_profile.setter
    def service_domain_service_subscriber_access_profile(self, service_domain_service_subscriber_access_profile):
        """Sets the service_domain_service_subscriber_access_profile of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The allowed service access for a user or subscriber to the service which can be any known party   # noqa: E501

        :param service_domain_service_subscriber_access_profile: The service_domain_service_subscriber_access_profile of this SDCurrentAccountActivateOutputModelServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription.
        :type service_domain_service_subscriber_access_profile: str
        """

        self._service_domain_service_subscriber_access_profile = service_domain_service_subscriber_access_profile
