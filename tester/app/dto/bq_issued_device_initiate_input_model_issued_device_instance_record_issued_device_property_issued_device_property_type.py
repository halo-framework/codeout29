# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_property_value=None):  # noqa: E501
        """BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType - a model defined in OpenAPI

        :param issued_device_property_value: The issued_device_property_value of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.  # noqa: E501
        :type issued_device_property_value: str
        """
        self.openapi_types = {
            'issued_device_property_value': str
        }

        self.attribute_map = {
            'issued_device_property_value': 'issuedDevicePropertyValue'
        }

        self._issued_device_property_value = issued_device_property_value

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceInitiateInputModel_issuedDeviceInstanceRecord_issuedDeviceProperty_issuedDevicePropertyType of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.  # noqa: E501
        :rtype: BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_property_value(self):
        """Gets the issued_device_property_value of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The tracked values associated with an issued device/inventory item   # noqa: E501

        :return: The issued_device_property_value of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.
        :rtype: str
        """
        return self._issued_device_property_value

    @issued_device_property_value.setter
    def issued_device_property_value(self, issued_device_property_value):
        """Sets the issued_device_property_value of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The tracked values associated with an issued device/inventory item   # noqa: E501

        :param issued_device_property_value: The issued_device_property_value of this BQIssuedDeviceInitiateInputModelIssuedDeviceInstanceRecordIssuedDevicePropertyIssuedDevicePropertyType.
        :type issued_device_property_value: str
        """

        self._issued_device_property_value = issued_device_property_value
