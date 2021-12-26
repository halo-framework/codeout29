# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2002_service_domain_offered_service_service_domain_service_record import InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
from tester import util

from tester.app.dto.inline_response2002_service_domain_offered_service_service_domain_service_record import InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord  # noqa: E501



class SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_reference=None, service_domain_service_record=None):  # noqa: E501
        """SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService - a model defined in OpenAPI

        :param service_domain_service_reference: The service_domain_service_reference of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.  # noqa: E501
        :type service_domain_service_reference: str
        :param service_domain_service_record: The service_domain_service_record of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.  # noqa: E501
        :type service_domain_service_record: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
        """
        self.openapi_types = {
            'service_domain_service_reference': str,
            'service_domain_service_record': InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
        }

        self.attribute_map = {
            'service_domain_service_reference': 'serviceDomainServiceReference',
            'service_domain_service_record': 'serviceDomainServiceRecord'
        }

        self._service_domain_service_reference = service_domain_service_reference
        self._service_domain_service_record = service_domain_service_record

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountRetrieveOutputModel_serviceDomainOfferedService of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.  # noqa: E501
        :rtype: SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_reference(self):
        """Gets the service_domain_service_reference of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a service offered by the service center   # noqa: E501

        :return: The service_domain_service_reference of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.
        :rtype: str
        """
        return self._service_domain_service_reference

    @service_domain_service_reference.setter
    def service_domain_service_reference(self, service_domain_service_reference):
        """Sets the service_domain_service_reference of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a service offered by the service center   # noqa: E501

        :param service_domain_service_reference: The service_domain_service_reference of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.
        :type service_domain_service_reference: str
        """

        self._service_domain_service_reference = service_domain_service_reference

    @property
    def service_domain_service_record(self):
        """Gets the service_domain_service_record of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.


        :return: The service_domain_service_record of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.
        :rtype: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
        """
        return self._service_domain_service_record

    @service_domain_service_record.setter
    def service_domain_service_record(self, service_domain_service_record):
        """Sets the service_domain_service_record of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.


        :param service_domain_service_record: The service_domain_service_record of this SDCurrentAccountRetrieveOutputModelServiceDomainOfferedService.
        :type service_domain_service_record: InlineResponse2002ServiceDomainOfferedServiceServiceDomainServiceRecord
        """

        self._service_domain_service_record = service_domain_service_record
