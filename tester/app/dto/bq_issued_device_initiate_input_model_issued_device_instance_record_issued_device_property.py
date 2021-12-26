# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property_issued_device_property_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property_issued_device_property_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType  # noqa: E501



class BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_property_type=None, issued_device_status=None):  # noqa: E501
        """BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty - a model defined in OpenAPI

        :param issued_device_property_type: The issued_device_property_type of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.  # noqa: E501
        :type issued_device_property_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType
        :param issued_device_status: The issued_device_status of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.  # noqa: E501
        :type issued_device_status: str
        """
        self.openapi_types = {
            'issued_device_property_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType,
            'issued_device_status': str
        }

        self.attribute_map = {
            'issued_device_property_type': 'issuedDevicePropertyType',
            'issued_device_status': 'issuedDeviceStatus'
        }

        self._issued_device_property_type = issued_device_property_type
        self._issued_device_status = issued_device_status

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceInitiateInputModel_issuedDeviceInstanceRecord_issuedDeviceProperty of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.  # noqa: E501
        :rtype: BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_property_type(self):
        """Gets the issued_device_property_type of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.


        :return: The issued_device_property_type of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType
        """
        return self._issued_device_property_type

    @issued_device_property_type.setter
    def issued_device_property_type(self, issued_device_property_type):
        """Sets the issued_device_property_type of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.


        :param issued_device_property_type: The issued_device_property_type of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.
        :type issued_device_property_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType
        """

        self._issued_device_property_type = issued_device_property_type

    @property
    def issued_device_status(self):
        """Gets the issued_device_status of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The tracked status of the device/inventory item (e.g. active, suspended, cancelled)   # noqa: E501

        :return: The issued_device_status of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.
        :rtype: str
        """
        return self._issued_device_status

    @issued_device_status.setter
    def issued_device_status(self, issued_device_status):
        """Sets the issued_device_status of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The tracked status of the device/inventory item (e.g. active, suspended, cancelled)   # noqa: E501

        :param issued_device_status: The issued_device_status of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDeviceProperty.
        :type issued_device_status: str
        """

        self._issued_device_status = issued_device_status