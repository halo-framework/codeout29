# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
from tester.app.dto.inline_response20024_issued_device_instance_analysis import InlineResponse20024IssuedDeviceInstanceAnalysis
from tester.app.dto.inline_response20024_issued_device_instance_report import InlineResponse20024IssuedDeviceInstanceReport
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord  # noqa: E501
from tester.app.dto.inline_response20024_issued_device_instance_analysis import InlineResponse20024IssuedDeviceInstanceAnalysis  # noqa: E501
from tester.app.dto.inline_response20024_issued_device_instance_report import InlineResponse20024IssuedDeviceInstanceReport  # noqa: E501



class InlineResponse20024(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_instance_record=None, issued_device_retrieve_action_task_reference=None, issued_device_retrieve_action_task_record=None, issued_device_retrieve_action_response=None, issued_device_instance_report=None, issued_device_instance_analysis=None):  # noqa: E501
        """InlineResponse20024 - a model defined in OpenAPI

        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse20024.  # noqa: E501
        :type issued_device_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        :param issued_device_retrieve_action_task_reference: The issued_device_retrieve_action_task_reference of this InlineResponse20024.  # noqa: E501
        :type issued_device_retrieve_action_task_reference: str
        :param issued_device_retrieve_action_task_record: The issued_device_retrieve_action_task_record of this InlineResponse20024.  # noqa: E501
        :type issued_device_retrieve_action_task_record: object
        :param issued_device_retrieve_action_response: The issued_device_retrieve_action_response of this InlineResponse20024.  # noqa: E501
        :type issued_device_retrieve_action_response: str
        :param issued_device_instance_report: The issued_device_instance_report of this InlineResponse20024.  # noqa: E501
        :type issued_device_instance_report: InlineResponse20024IssuedDeviceInstanceReport
        :param issued_device_instance_analysis: The issued_device_instance_analysis of this InlineResponse20024.  # noqa: E501
        :type issued_device_instance_analysis: InlineResponse20024IssuedDeviceInstanceAnalysis
        """
        self.openapi_types = {
            'issued_device_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord,
            'issued_device_retrieve_action_task_reference': str,
            'issued_device_retrieve_action_task_record': object,
            'issued_device_retrieve_action_response': str,
            'issued_device_instance_report': InlineResponse20024IssuedDeviceInstanceReport,
            'issued_device_instance_analysis': InlineResponse20024IssuedDeviceInstanceAnalysis
        }

        self.attribute_map = {
            'issued_device_instance_record': 'issuedDeviceInstanceRecord',
            'issued_device_retrieve_action_task_reference': 'issuedDeviceRetrieveActionTaskReference',
            'issued_device_retrieve_action_task_record': 'issuedDeviceRetrieveActionTaskRecord',
            'issued_device_retrieve_action_response': 'issuedDeviceRetrieveActionResponse',
            'issued_device_instance_report': 'issuedDeviceInstanceReport',
            'issued_device_instance_analysis': 'issuedDeviceInstanceAnalysis'
        }

        self._issued_device_instance_record = issued_device_instance_record
        self._issued_device_retrieve_action_task_reference = issued_device_retrieve_action_task_reference
        self._issued_device_retrieve_action_task_record = issued_device_retrieve_action_task_record
        self._issued_device_retrieve_action_response = issued_device_retrieve_action_response
        self._issued_device_instance_report = issued_device_instance_report
        self._issued_device_instance_analysis = issued_device_instance_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20024':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_24 of this InlineResponse20024.  # noqa: E501
        :rtype: InlineResponse20024
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_instance_record(self):
        """Gets the issued_device_instance_record of this InlineResponse20024.


        :return: The issued_device_instance_record of this InlineResponse20024.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        """
        return self._issued_device_instance_record

    @issued_device_instance_record.setter
    def issued_device_instance_record(self, issued_device_instance_record):
        """Sets the issued_device_instance_record of this InlineResponse20024.


        :param issued_device_instance_record: The issued_device_instance_record of this InlineResponse20024.
        :type issued_device_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        """

        self._issued_device_instance_record = issued_device_instance_record

    @property
    def issued_device_retrieve_action_task_reference(self):
        """Gets the issued_device_retrieve_action_task_reference of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Issued Device instance retrieve service call   # noqa: E501

        :return: The issued_device_retrieve_action_task_reference of this InlineResponse20024.
        :rtype: str
        """
        return self._issued_device_retrieve_action_task_reference

    @issued_device_retrieve_action_task_reference.setter
    def issued_device_retrieve_action_task_reference(self, issued_device_retrieve_action_task_reference):
        """Sets the issued_device_retrieve_action_task_reference of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to a Issued Device instance retrieve service call   # noqa: E501

        :param issued_device_retrieve_action_task_reference: The issued_device_retrieve_action_task_reference of this InlineResponse20024.
        :type issued_device_retrieve_action_task_reference: str
        """

        self._issued_device_retrieve_action_task_reference = issued_device_retrieve_action_task_reference

    @property
    def issued_device_retrieve_action_task_record(self):
        """Gets the issued_device_retrieve_action_task_record of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :return: The issued_device_retrieve_action_task_record of this InlineResponse20024.
        :rtype: object
        """
        return self._issued_device_retrieve_action_task_record

    @issued_device_retrieve_action_task_record.setter
    def issued_device_retrieve_action_task_record(self, issued_device_retrieve_action_task_record):
        """Sets the issued_device_retrieve_action_task_record of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :param issued_device_retrieve_action_task_record: The issued_device_retrieve_action_task_record of this InlineResponse20024.
        :type issued_device_retrieve_action_task_record: object
        """

        self._issued_device_retrieve_action_task_record = issued_device_retrieve_action_task_record

    @property
    def issued_device_retrieve_action_response(self):
        """Gets the issued_device_retrieve_action_response of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :return: The issued_device_retrieve_action_response of this InlineResponse20024.
        :rtype: str
        """
        return self._issued_device_retrieve_action_response

    @issued_device_retrieve_action_response.setter
    def issued_device_retrieve_action_response(self, issued_device_retrieve_action_response):
        """Sets the issued_device_retrieve_action_response of this InlineResponse20024.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service response (lists returned reports)   # noqa: E501

        :param issued_device_retrieve_action_response: The issued_device_retrieve_action_response of this InlineResponse20024.
        :type issued_device_retrieve_action_response: str
        """

        self._issued_device_retrieve_action_response = issued_device_retrieve_action_response

    @property
    def issued_device_instance_report(self):
        """Gets the issued_device_instance_report of this InlineResponse20024.


        :return: The issued_device_instance_report of this InlineResponse20024.
        :rtype: InlineResponse20024IssuedDeviceInstanceReport
        """
        return self._issued_device_instance_report

    @issued_device_instance_report.setter
    def issued_device_instance_report(self, issued_device_instance_report):
        """Sets the issued_device_instance_report of this InlineResponse20024.


        :param issued_device_instance_report: The issued_device_instance_report of this InlineResponse20024.
        :type issued_device_instance_report: InlineResponse20024IssuedDeviceInstanceReport
        """

        self._issued_device_instance_report = issued_device_instance_report

    @property
    def issued_device_instance_analysis(self):
        """Gets the issued_device_instance_analysis of this InlineResponse20024.


        :return: The issued_device_instance_analysis of this InlineResponse20024.
        :rtype: InlineResponse20024IssuedDeviceInstanceAnalysis
        """
        return self._issued_device_instance_analysis

    @issued_device_instance_analysis.setter
    def issued_device_instance_analysis(self, issued_device_instance_analysis):
        """Sets the issued_device_instance_analysis of this InlineResponse20024.


        :param issued_device_instance_analysis: The issued_device_instance_analysis of this InlineResponse20024.
        :type issued_device_instance_analysis: InlineResponse20024IssuedDeviceInstanceAnalysis
        """

        self._issued_device_instance_analysis = issued_device_instance_analysis
