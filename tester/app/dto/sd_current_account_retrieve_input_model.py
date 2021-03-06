# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_offered_service1 import SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1 import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1
from tester import util

from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_offered_service1 import SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1  # noqa: E501
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1 import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1  # noqa: E501



class SDCurrentAccountRetrieveInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_retrieve_action_task_record=None, service_domain_retrieve_action_request=None, service_domain_retrieve_action_record=None, service_domain_offered_service=None):  # noqa: E501
        """SDCurrentAccountRetrieveInputModel - a model defined in OpenAPI

        :param service_domain_retrieve_action_task_record: The service_domain_retrieve_action_task_record of this SDCurrentAccountRetrieveInputModel.  # noqa: E501
        :type service_domain_retrieve_action_task_record: object
        :param service_domain_retrieve_action_request: The service_domain_retrieve_action_request of this SDCurrentAccountRetrieveInputModel.  # noqa: E501
        :type service_domain_retrieve_action_request: str
        :param service_domain_retrieve_action_record: The service_domain_retrieve_action_record of this SDCurrentAccountRetrieveInputModel.  # noqa: E501
        :type service_domain_retrieve_action_record: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1
        :param service_domain_offered_service: The service_domain_offered_service of this SDCurrentAccountRetrieveInputModel.  # noqa: E501
        :type service_domain_offered_service: SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1
        """
        self.openapi_types = {
            'service_domain_retrieve_action_task_record': object,
            'service_domain_retrieve_action_request': str,
            'service_domain_retrieve_action_record': SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1,
            'service_domain_offered_service': SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1
        }

        self.attribute_map = {
            'service_domain_retrieve_action_task_record': 'serviceDomainRetrieveActionTaskRecord',
            'service_domain_retrieve_action_request': 'serviceDomainRetrieveActionRequest',
            'service_domain_retrieve_action_record': 'serviceDomainRetrieveActionRecord',
            'service_domain_offered_service': 'serviceDomainOfferedService'
        }

        self._service_domain_retrieve_action_task_record = service_domain_retrieve_action_task_record
        self._service_domain_retrieve_action_request = service_domain_retrieve_action_request
        self._service_domain_retrieve_action_record = service_domain_retrieve_action_record
        self._service_domain_offered_service = service_domain_offered_service

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountRetrieveInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountRetrieveInputModel of this SDCurrentAccountRetrieveInputModel.  # noqa: E501
        :rtype: SDCurrentAccountRetrieveInputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_retrieve_action_task_record(self):
        """Gets the service_domain_retrieve_action_task_record of this SDCurrentAccountRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :return: The service_domain_retrieve_action_task_record of this SDCurrentAccountRetrieveInputModel.
        :rtype: object
        """
        return self._service_domain_retrieve_action_task_record

    @service_domain_retrieve_action_task_record.setter
    def service_domain_retrieve_action_task_record(self, service_domain_retrieve_action_task_record):
        """Sets the service_domain_retrieve_action_task_record of this SDCurrentAccountRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :param service_domain_retrieve_action_task_record: The service_domain_retrieve_action_task_record of this SDCurrentAccountRetrieveInputModel.
        :type service_domain_retrieve_action_task_record: object
        """

        self._service_domain_retrieve_action_task_record = service_domain_retrieve_action_task_record

    @property
    def service_domain_retrieve_action_request(self):
        """Gets the service_domain_retrieve_action_request of this SDCurrentAccountRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service request (lists requested reports)   # noqa: E501

        :return: The service_domain_retrieve_action_request of this SDCurrentAccountRetrieveInputModel.
        :rtype: str
        """
        return self._service_domain_retrieve_action_request

    @service_domain_retrieve_action_request.setter
    def service_domain_retrieve_action_request(self, service_domain_retrieve_action_request):
        """Sets the service_domain_retrieve_action_request of this SDCurrentAccountRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service request (lists requested reports)   # noqa: E501

        :param service_domain_retrieve_action_request: The service_domain_retrieve_action_request of this SDCurrentAccountRetrieveInputModel.
        :type service_domain_retrieve_action_request: str
        """

        self._service_domain_retrieve_action_request = service_domain_retrieve_action_request

    @property
    def service_domain_retrieve_action_record(self):
        """Gets the service_domain_retrieve_action_record of this SDCurrentAccountRetrieveInputModel.


        :return: The service_domain_retrieve_action_record of this SDCurrentAccountRetrieveInputModel.
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1
        """
        return self._service_domain_retrieve_action_record

    @service_domain_retrieve_action_record.setter
    def service_domain_retrieve_action_record(self, service_domain_retrieve_action_record):
        """Sets the service_domain_retrieve_action_record of this SDCurrentAccountRetrieveInputModel.


        :param service_domain_retrieve_action_record: The service_domain_retrieve_action_record of this SDCurrentAccountRetrieveInputModel.
        :type service_domain_retrieve_action_record: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1
        """

        self._service_domain_retrieve_action_record = service_domain_retrieve_action_record

    @property
    def service_domain_offered_service(self):
        """Gets the service_domain_offered_service of this SDCurrentAccountRetrieveInputModel.


        :return: The service_domain_offered_service of this SDCurrentAccountRetrieveInputModel.
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1
        """
        return self._service_domain_offered_service

    @service_domain_offered_service.setter
    def service_domain_offered_service(self, service_domain_offered_service):
        """Sets the service_domain_offered_service of this SDCurrentAccountRetrieveInputModel.


        :param service_domain_offered_service: The service_domain_offered_service of this SDCurrentAccountRetrieveInputModel.
        :type service_domain_offered_service: SDCurrentAccountRetrieveInputModelServiceDomainOfferedService1
        """

        self._service_domain_offered_service = service_domain_offered_service
