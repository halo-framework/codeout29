# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_agreement import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement
from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_configuration_setup import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_subscription import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription
from tester import util

from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_agreement import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_configuration_setup import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_configuration_service_domain_service_configuration_record_service_domain_service_subscription import CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription  # noqa: E501



class SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_service_configuration_setting_description=None, service_domain_service_configuration_setup=None, service_domain_service_subscription=None, service_domain_service_agreement=None, service_domain_service_status=None):  # noqa: E501
        """SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord - a model defined in OpenAPI

        :param service_domain_service_configuration_setting_description: The service_domain_service_configuration_setting_description of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_configuration_setting_description: str
        :param service_domain_service_configuration_setup: The service_domain_service_configuration_setup of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_configuration_setup: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        :param service_domain_service_subscription: The service_domain_service_subscription of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_subscription: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription
        :param service_domain_service_agreement: The service_domain_service_agreement of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_agreement: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement
        :param service_domain_service_status: The service_domain_service_status of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :type service_domain_service_status: str
        """
        self.openapi_types = {
            'service_domain_service_configuration_setting_description': str,
            'service_domain_service_configuration_setup': CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup,
            'service_domain_service_subscription': CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription,
            'service_domain_service_agreement': CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement,
            'service_domain_service_status': str
        }

        self.attribute_map = {
            'service_domain_service_configuration_setting_description': 'serviceDomainServiceConfigurationSettingDescription',
            'service_domain_service_configuration_setup': 'serviceDomainServiceConfigurationSetup',
            'service_domain_service_subscription': 'serviceDomainServiceSubscription',
            'service_domain_service_agreement': 'serviceDomainServiceAgreement',
            'service_domain_service_status': 'serviceDomainServiceStatus'
        }

        self._service_domain_service_configuration_setting_description = service_domain_service_configuration_setting_description
        self._service_domain_service_configuration_setup = service_domain_service_configuration_setup
        self._service_domain_service_subscription = service_domain_service_subscription
        self._service_domain_service_agreement = service_domain_service_agreement
        self._service_domain_service_status = service_domain_service_status

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountConfigureOutputModel_serviceDomainServiceConfigurationRecord of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.  # noqa: E501
        :rtype: SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_service_configuration_setting_description(self):
        """Gets the service_domain_service_configuration_setting_description of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the configuration parameter, allowed values and processing impact   # noqa: E501

        :return: The service_domain_service_configuration_setting_description of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :rtype: str
        """
        return self._service_domain_service_configuration_setting_description

    @service_domain_service_configuration_setting_description.setter
    def service_domain_service_configuration_setting_description(self, service_domain_service_configuration_setting_description):
        """Sets the service_domain_service_configuration_setting_description of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the configuration parameter, allowed values and processing impact   # noqa: E501

        :param service_domain_service_configuration_setting_description: The service_domain_service_configuration_setting_description of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :type service_domain_service_configuration_setting_description: str
        """

        self._service_domain_service_configuration_setting_description = service_domain_service_configuration_setting_description

    @property
    def service_domain_service_configuration_setup(self):
        """Gets the service_domain_service_configuration_setup of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :return: The service_domain_service_configuration_setup of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :rtype: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        """
        return self._service_domain_service_configuration_setup

    @service_domain_service_configuration_setup.setter
    def service_domain_service_configuration_setup(self, service_domain_service_configuration_setup):
        """Sets the service_domain_service_configuration_setup of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :param service_domain_service_configuration_setup: The service_domain_service_configuration_setup of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :type service_domain_service_configuration_setup: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceConfigurationSetup
        """

        self._service_domain_service_configuration_setup = service_domain_service_configuration_setup

    @property
    def service_domain_service_subscription(self):
        """Gets the service_domain_service_subscription of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :return: The service_domain_service_subscription of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :rtype: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription
        """
        return self._service_domain_service_subscription

    @service_domain_service_subscription.setter
    def service_domain_service_subscription(self, service_domain_service_subscription):
        """Sets the service_domain_service_subscription of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :param service_domain_service_subscription: The service_domain_service_subscription of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :type service_domain_service_subscription: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceSubscription
        """

        self._service_domain_service_subscription = service_domain_service_subscription

    @property
    def service_domain_service_agreement(self):
        """Gets the service_domain_service_agreement of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :return: The service_domain_service_agreement of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :rtype: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement
        """
        return self._service_domain_service_agreement

    @service_domain_service_agreement.setter
    def service_domain_service_agreement(self, service_domain_service_agreement):
        """Sets the service_domain_service_agreement of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.


        :param service_domain_service_agreement: The service_domain_service_agreement of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :type service_domain_service_agreement: CurrentAccountSdReferenceIdConfigurationServiceDomainServiceConfigurationRecordServiceDomainServiceAgreement
        """

        self._service_domain_service_agreement = service_domain_service_agreement

    @property
    def service_domain_service_status(self):
        """Gets the service_domain_service_status of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the offered service (e.g. active, suspended, idle)   # noqa: E501

        :return: The service_domain_service_status of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :rtype: str
        """
        return self._service_domain_service_status

    @service_domain_service_status.setter
    def service_domain_service_status(self, service_domain_service_status):
        """Sets the service_domain_service_status of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status of the offered service (e.g. active, suspended, idle)   # noqa: E501

        :param service_domain_service_status: The service_domain_service_status of this SDCurrentAccountConfigureOutputModelServiceDomainServiceConfigurationRecord.
        :type service_domain_service_status: str
        """

        self._service_domain_service_status = service_domain_service_status
