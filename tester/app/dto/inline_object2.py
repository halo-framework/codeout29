# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_feedback_service_domain_feedback_action_record import CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_feedback_service_domain_feedback_action_record import CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord  # noqa: E501



class InlineObject2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_feedback_action_task_record=None, service_domain_feedback_action_record=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI

        :param service_domain_feedback_action_task_record: The service_domain_feedback_action_task_record of this InlineObject2.  # noqa: E501
        :type service_domain_feedback_action_task_record: object
        :param service_domain_feedback_action_record: The service_domain_feedback_action_record of this InlineObject2.  # noqa: E501
        :type service_domain_feedback_action_record: CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord
        """
        self.openapi_types = {
            'service_domain_feedback_action_task_record': object,
            'service_domain_feedback_action_record': CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord
        }

        self.attribute_map = {
            'service_domain_feedback_action_task_record': 'serviceDomainFeedbackActionTaskRecord',
            'service_domain_feedback_action_record': 'serviceDomainFeedbackActionRecord'
        }

        self._service_domain_feedback_action_task_record = service_domain_feedback_action_task_record
        self._service_domain_feedback_action_record = service_domain_feedback_action_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_2 of this InlineObject2.  # noqa: E501
        :rtype: InlineObject2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_feedback_action_task_record(self):
        """Gets the service_domain_feedback_action_task_record of this InlineObject2.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The feedback service call consolidated processing record   # noqa: E501

        :return: The service_domain_feedback_action_task_record of this InlineObject2.
        :rtype: object
        """
        return self._service_domain_feedback_action_task_record

    @service_domain_feedback_action_task_record.setter
    def service_domain_feedback_action_task_record(self, service_domain_feedback_action_task_record):
        """Sets the service_domain_feedback_action_task_record of this InlineObject2.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The feedback service call consolidated processing record   # noqa: E501

        :param service_domain_feedback_action_task_record: The service_domain_feedback_action_task_record of this InlineObject2.
        :type service_domain_feedback_action_task_record: object
        """

        self._service_domain_feedback_action_task_record = service_domain_feedback_action_task_record

    @property
    def service_domain_feedback_action_record(self):
        """Gets the service_domain_feedback_action_record of this InlineObject2.


        :return: The service_domain_feedback_action_record of this InlineObject2.
        :rtype: CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord
        """
        return self._service_domain_feedback_action_record

    @service_domain_feedback_action_record.setter
    def service_domain_feedback_action_record(self, service_domain_feedback_action_record):
        """Sets the service_domain_feedback_action_record of this InlineObject2.


        :param service_domain_feedback_action_record: The service_domain_feedback_action_record of this InlineObject2.
        :type service_domain_feedback_action_record: CurrentAccountSdReferenceIdFeedbackServiceDomainFeedbackActionRecord
        """

        self._service_domain_feedback_action_record = service_domain_feedback_action_record
