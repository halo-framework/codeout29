# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_agreement_reference=None, service_domain_service_user_reference=None, service_domain_service_agreement_termsand_conditions=None):  # noqa: E501
        """SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement - a model defined in OpenAPI

        :param service_domain_service_agreement_reference: The service_domain_service_agreement_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.  # noqa: E501
        :type service_domain_service_agreement_reference: str
        :param service_domain_service_user_reference: The service_domain_service_user_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.  # noqa: E501
        :type service_domain_service_user_reference: str
        :param service_domain_service_agreement_termsand_conditions: The service_domain_service_agreement_termsand_conditions of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.  # noqa: E501
        :type service_domain_service_agreement_termsand_conditions: str
        """
        self.openapi_types = {
            'service_domain_service_agreement_reference': str,
            'service_domain_service_user_reference': str,
            'service_domain_service_agreement_termsand_conditions': str
        }

        self.attribute_map = {
            'service_domain_service_agreement_reference': 'serviceDomainServiceAgreementReference',
            'service_domain_service_user_reference': 'serviceDomainServiceUserReference',
            'service_domain_service_agreement_termsand_conditions': 'serviceDomainServiceAgreementTermsandConditions'
        }

        self._service_domain_service_agreement_reference = service_domain_service_agreement_reference
        self._service_domain_service_user_reference = service_domain_service_user_reference
        self._service_domain_service_agreement_termsand_conditions = service_domain_service_agreement_termsand_conditions

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountConfigureInputModel_serviceDomainServiceConfigurationRecord_serviceDomainServiceAgreement of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.  # noqa: E501
        :rtype: SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_agreement_reference(self):
        """Gets the service_domain_service_agreement_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the offered service agreement   # noqa: E501

        :return: The service_domain_service_agreement_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :rtype: str
        """
        return self._service_domain_service_agreement_reference

    @service_domain_service_agreement_reference.setter
    def service_domain_service_agreement_reference(self, service_domain_service_agreement_reference):
        """Sets the service_domain_service_agreement_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the offered service agreement   # noqa: E501

        :param service_domain_service_agreement_reference: The service_domain_service_agreement_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :type service_domain_service_agreement_reference: str
        """

        self._service_domain_service_agreement_reference = service_domain_service_agreement_reference

    @property
    def service_domain_service_user_reference(self):
        """Gets the service_domain_service_user_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the user covered by the contract   # noqa: E501

        :return: The service_domain_service_user_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :rtype: str
        """
        return self._service_domain_service_user_reference

    @service_domain_service_user_reference.setter
    def service_domain_service_user_reference(self, service_domain_service_user_reference):
        """Sets the service_domain_service_user_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the user covered by the contract   # noqa: E501

        :param service_domain_service_user_reference: The service_domain_service_user_reference of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :type service_domain_service_user_reference: str
        """

        self._service_domain_service_user_reference = service_domain_service_user_reference

    @property
    def service_domain_service_agreement_termsand_conditions(self):
        """Gets the service_domain_service_agreement_termsand_conditions of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Terms and conditions covering the service agreement   # noqa: E501

        :return: The service_domain_service_agreement_termsand_conditions of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :rtype: str
        """
        return self._service_domain_service_agreement_termsand_conditions

    @service_domain_service_agreement_termsand_conditions.setter
    def service_domain_service_agreement_termsand_conditions(self, service_domain_service_agreement_termsand_conditions):
        """Sets the service_domain_service_agreement_termsand_conditions of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Terms and conditions covering the service agreement   # noqa: E501

        :param service_domain_service_agreement_termsand_conditions: The service_domain_service_agreement_termsand_conditions of this SDCurrentAccountConfigureInputModelServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement.
        :type service_domain_service_agreement_termsand_conditions: str
        """

        self._service_domain_service_agreement_termsand_conditions = service_domain_service_agreement_termsand_conditions