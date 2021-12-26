# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty  # noqa: E501



class BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_type=None, issued_device_option_setting=None, issued_device_property=None):  # noqa: E501
        """BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord - a model defined in OpenAPI

        :param issued_device_type: The issued_device_type of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_type: str
        :param issued_device_option_setting: The issued_device_option_setting of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_option_setting: str
        :param issued_device_property: The issued_device_property of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_property: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """
        self.openapi_types = {
            'issued_device_type': str,
            'issued_device_option_setting': str,
            'issued_device_property': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        }

        self.attribute_map = {
            'issued_device_type': 'issuedDeviceType',
            'issued_device_option_setting': 'issuedDeviceOptionSetting',
            'issued_device_property': 'issuedDeviceProperty'
        }

        self._issued_device_type = issued_device_type
        self._issued_device_option_setting = issued_device_option_setting
        self._issued_device_property = issued_device_property

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceRequestInputModel_issuedDeviceInstanceRecord of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.  # noqa: E501
        :rtype: BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_type(self):
        """Gets the issued_device_type of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of issued device/inventory (e.g. checkbook, pay-in slip)   # noqa: E501

        :return: The issued_device_type of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_type

    @issued_device_type.setter
    def issued_device_type(self, issued_device_type):
        """Sets the issued_device_type of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of issued device/inventory (e.g. checkbook, pay-in slip)   # noqa: E501

        :param issued_device_type: The issued_device_type of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :type issued_device_type: str
        """

        self._issued_device_type = issued_device_type

    @property
    def issued_device_option_setting(self):
        """Gets the issued_device_option_setting of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option setting    # noqa: E501

        :return: The issued_device_option_setting of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_option_setting

    @issued_device_option_setting.setter
    def issued_device_option_setting(self, issued_device_option_setting):
        """Sets the issued_device_option_setting of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option setting    # noqa: E501

        :param issued_device_option_setting: The issued_device_option_setting of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :type issued_device_option_setting: str
        """

        self._issued_device_option_setting = issued_device_option_setting

    @property
    def issued_device_property(self):
        """Gets the issued_device_property of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.


        :return: The issued_device_property of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """
        return self._issued_device_property

    @issued_device_property.setter
    def issued_device_property(self, issued_device_property):
        """Sets the issued_device_property of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.


        :param issued_device_property: The issued_device_property of this BQIssuedDeviceRequestInputModelIssuedDeviceInstanceRecord.
        :type issued_device_property: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """

        self._issued_device_property = issued_device_property