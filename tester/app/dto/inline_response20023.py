# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2017_issued_device_instance_record import InlineResponse2017IssuedDeviceInstanceRecord
from tester import util

from tester.app.dto.inline_response2017_issued_device_instance_record import InlineResponse2017IssuedDeviceInstanceRecord  # noqa: E501



class InlineResponse20023(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_instance_record=None, issued_device_request_action_task_reference=None, issued_device_request_action_task_record=None, issued_device_request_record_reference=None, request_response_record=None):  # noqa: E501
        """InlineResponse20023 - a model defined in OpenAPI

        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse20023.  # noqa: E501
        :type issued_device_instance_record: InlineResponse2017IssuedDeviceInstanceRecord
        :param issued_device_request_action_task_reference: The issued_device_request_action_task_reference of this InlineResponse20023.  # noqa: E501
        :type issued_device_request_action_task_reference: str
        :param issued_device_request_action_task_record: The issued_device_request_action_task_record of this InlineResponse20023.  # noqa: E501
        :type issued_device_request_action_task_record: object
        :param issued_device_request_record_reference: The issued_device_request_record_reference of this InlineResponse20023.  # noqa: E501
        :type issued_device_request_record_reference: str
        :param request_response_record: The request_response_record of this InlineResponse20023.  # noqa: E501
        :type request_response_record: object
        """
        self.openapi_types = {
            'issued_device_instance_record': InlineResponse2017IssuedDeviceInstanceRecord,
            'issued_device_request_action_task_reference': str,
            'issued_device_request_action_task_record': object,
            'issued_device_request_record_reference': str,
            'request_response_record': object
        }

        self.attribute_map = {
            'issued_device_instance_record': 'issuedDeviceInstanceRecord',
            'issued_device_request_action_task_reference': 'issuedDeviceRequestActionTaskReference',
            'issued_device_request_action_task_record': 'issuedDeviceRequestActionTaskRecord',
            'issued_device_request_record_reference': 'issuedDeviceRequestRecordReference',
            'request_response_record': 'requestResponseRecord'
        }

        self._issued_device_instance_record = issued_device_instance_record
        self._issued_device_request_action_task_reference = issued_device_request_action_task_reference
        self._issued_device_request_action_task_record = issued_device_request_action_task_record
        self._issued_device_request_record_reference = issued_device_request_record_reference
        self._request_response_record = request_response_record

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20023':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_23 of this InlineResponse20023.  # noqa: E501
        :rtype: InlineResponse20023
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_instance_record(self):
        """Gets the issued_device_instance_record of this InlineResponse20023.


        :return: The issued_device_instance_record of this InlineResponse20023.
        :rtype: InlineResponse2017IssuedDeviceInstanceRecord
        """
        return self._issued_device_instance_record

    @issued_device_instance_record.setter
    def issued_device_instance_record(self, issued_device_instance_record):
        """Sets the issued_device_instance_record of this InlineResponse20023.


        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse20023.
        :type issued_device_instance_record: InlineResponse2017IssuedDeviceInstanceRecord
        """

        self._issued_device_instance_record = issued_device_instance_record

    @property
    def issued_device_request_action_task_reference(self):
        """Gets the issued_device_request_action_task_reference of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Issued Device instance request service call   # noqa: E501

        :return: The issued_device_request_action_task_reference of this InlineResponse20023.
        :rtype: str
        """
        return self._issued_device_request_action_task_reference

    @issued_device_request_action_task_reference.setter
    def issued_device_request_action_task_reference(self, issued_device_request_action_task_reference):
        """Sets the issued_device_request_action_task_reference of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Issued Device instance request service call   # noqa: E501

        :param issued_device_request_action_task_reference: The issued_device_request_action_task_reference of this InlineResponse20023.
        :type issued_device_request_action_task_reference: str
        """

        self._issued_device_request_action_task_reference = issued_device_request_action_task_reference

    @property
    def issued_device_request_action_task_record(self):
        """Gets the issued_device_request_action_task_record of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The request service call consolidated processing record   # noqa: E501

        :return: The issued_device_request_action_task_record of this InlineResponse20023.
        :rtype: object
        """
        return self._issued_device_request_action_task_record

    @issued_device_request_action_task_record.setter
    def issued_device_request_action_task_record(self, issued_device_request_action_task_record):
        """Sets the issued_device_request_action_task_record of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The request service call consolidated processing record   # noqa: E501

        :param issued_device_request_action_task_record: The issued_device_request_action_task_record of this InlineResponse20023.
        :type issued_device_request_action_task_record: object
        """

        self._issued_device_request_action_task_record = issued_device_request_action_task_record

    @property
    def issued_device_request_record_reference(self):
        """Gets the issued_device_request_record_reference of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Issued Device service request record   # noqa: E501

        :return: The issued_device_request_record_reference of this InlineResponse20023.
        :rtype: str
        """
        return self._issued_device_request_record_reference

    @issued_device_request_record_reference.setter
    def issued_device_request_record_reference(self, issued_device_request_record_reference):
        """Sets the issued_device_request_record_reference of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the Issued Device service request record   # noqa: E501

        :param issued_device_request_record_reference: The issued_device_request_record_reference of this InlineResponse20023.
        :type issued_device_request_record_reference: str
        """

        self._issued_device_request_record_reference = issued_device_request_record_reference

    @property
    def request_response_record(self):
        """Gets the request_response_record of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the request action service response   # noqa: E501

        :return: The request_response_record of this InlineResponse20023.
        :rtype: object
        """
        return self._request_response_record

    @request_response_record.setter
    def request_response_record(self, request_response_record):
        """Sets the request_response_record of this InlineResponse20023.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the request action service response   # noqa: E501

        :param request_response_record: The request_response_record of this InlineResponse20023.
        :type request_response_record: object
        """

        self._request_response_record = request_response_record
