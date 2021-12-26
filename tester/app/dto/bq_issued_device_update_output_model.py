# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord  # noqa: E501



class BQIssuedDeviceUpdateOutputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_instance_record=None, issued_device_update_action_task_reference=None, issued_device_update_action_task_record=None, update_response_record=None):  # noqa: E501
        """BQIssuedDeviceUpdateOutputModel - a model defined in OpenAPI

        :param issued_device_instance_record: The issued_device_instance_record of this BQIssuedDeviceUpdateOutputModel.  # noqa: E501
        :type issued_device_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        :param issued_device_update_action_task_reference: The issued_device_update_action_task_reference of this BQIssuedDeviceUpdateOutputModel.  # noqa: E501
        :type issued_device_update_action_task_reference: str
        :param issued_device_update_action_task_record: The issued_device_update_action_task_record of this BQIssuedDeviceUpdateOutputModel.  # noqa: E501
        :type issued_device_update_action_task_record: object
        :param update_response_record: The update_response_record of this BQIssuedDeviceUpdateOutputModel.  # noqa: E501
        :type update_response_record: object
        """
        self.openapi_types = {
            'issued_device_instance_record': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord,
            'issued_device_update_action_task_reference': str,
            'issued_device_update_action_task_record': object,
            'update_response_record': object
        }

        self.attribute_map = {
            'issued_device_instance_record': 'issuedDeviceInstanceRecord',
            'issued_device_update_action_task_reference': 'issuedDeviceUpdateActionTaskReference',
            'issued_device_update_action_task_record': 'issuedDeviceUpdateActionTaskRecord',
            'update_response_record': 'updateResponseRecord'
        }

        self._issued_device_instance_record = issued_device_instance_record
        self._issued_device_update_action_task_reference = issued_device_update_action_task_reference
        self._issued_device_update_action_task_record = issued_device_update_action_task_record
        self._update_response_record = update_response_record

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceUpdateOutputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceUpdateOutputModel of this BQIssuedDeviceUpdateOutputModel.  # noqa: E501
        :rtype: BQIssuedDeviceUpdateOutputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_instance_record(self):
        """Gets the issued_device_instance_record of this BQIssuedDeviceUpdateOutputModel.


        :return: The issued_device_instance_record of this BQIssuedDeviceUpdateOutputModel.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        """
        return self._issued_device_instance_record

    @issued_device_instance_record.setter
    def issued_device_instance_record(self, issued_device_instance_record):
        """Sets the issued_device_instance_record of this BQIssuedDeviceUpdateOutputModel.


        :param issued_device_instance_record: The issued_device_instance_record of this BQIssuedDeviceUpdateOutputModel.
        :type issued_device_instance_record: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        """

        self._issued_device_instance_record = issued_device_instance_record

    @property
    def issued_device_update_action_task_reference(self):
        """Gets the issued_device_update_action_task_reference of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :return: The issued_device_update_action_task_reference of this BQIssuedDeviceUpdateOutputModel.
        :rtype: str
        """
        return self._issued_device_update_action_task_reference

    @issued_device_update_action_task_reference.setter
    def issued_device_update_action_task_reference(self, issued_device_update_action_task_reference):
        """Sets the issued_device_update_action_task_reference of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to an update service call   # noqa: E501

        :param issued_device_update_action_task_reference: The issued_device_update_action_task_reference of this BQIssuedDeviceUpdateOutputModel.
        :type issued_device_update_action_task_reference: str
        """

        self._issued_device_update_action_task_reference = issued_device_update_action_task_reference

    @property
    def issued_device_update_action_task_record(self):
        """Gets the issued_device_update_action_task_record of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :return: The issued_device_update_action_task_record of this BQIssuedDeviceUpdateOutputModel.
        :rtype: object
        """
        return self._issued_device_update_action_task_record

    @issued_device_update_action_task_record.setter
    def issued_device_update_action_task_record(self, issued_device_update_action_task_record):
        """Sets the issued_device_update_action_task_record of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The update service call consolidated processing record   # noqa: E501

        :param issued_device_update_action_task_record: The issued_device_update_action_task_record of this BQIssuedDeviceUpdateOutputModel.
        :type issued_device_update_action_task_record: object
        """

        self._issued_device_update_action_task_record = issued_device_update_action_task_record

    @property
    def update_response_record(self):
        """Gets the update_response_record of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :return: The update_response_record of this BQIssuedDeviceUpdateOutputModel.
        :rtype: object
        """
        return self._update_response_record

    @update_response_record.setter
    def update_response_record(self, update_response_record):
        """Sets the update_response_record of this BQIssuedDeviceUpdateOutputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: Details of the Update action service response   # noqa: E501

        :param update_response_record: The update_response_record of this BQIssuedDeviceUpdateOutputModel.
        :type update_response_record: object
        """

        self._update_response_record = update_response_record
