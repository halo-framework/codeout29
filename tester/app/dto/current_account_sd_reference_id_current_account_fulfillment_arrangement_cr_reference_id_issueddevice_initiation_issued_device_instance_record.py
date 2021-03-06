# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_cr_reference_id_issueddevice_initiation_issued_device_instance_record_issued_device_property import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty  # noqa: E501



class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issued_device_type=None, issued_device_description=None, issued_device_option_definition=None, issued_device_option_setting=None, issued_device_property=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord - a model defined in OpenAPI

        :param issued_device_type: The issued_device_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_type: str
        :param issued_device_description: The issued_device_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_description: str
        :param issued_device_option_definition: The issued_device_option_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_option_definition: str
        :param issued_device_option_setting: The issued_device_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_option_setting: str
        :param issued_device_property: The issued_device_property of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :type issued_device_property: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """
        self.openapi_types = {
            'issued_device_type': str,
            'issued_device_description': str,
            'issued_device_option_definition': str,
            'issued_device_option_setting': str,
            'issued_device_property': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        }

        self.attribute_map = {
            'issued_device_type': 'issuedDeviceType',
            'issued_device_description': 'issuedDeviceDescription',
            'issued_device_option_definition': 'issuedDeviceOptionDefinition',
            'issued_device_option_setting': 'issuedDeviceOptionSetting',
            'issued_device_property': 'issuedDeviceProperty'
        }

        self._issued_device_type = issued_device_type
        self._issued_device_description = issued_device_description
        self._issued_device_option_definition = issued_device_option_definition
        self._issued_device_option_setting = issued_device_option_setting
        self._issued_device_property = issued_device_property

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__issueddevice_initiation_issuedDeviceInstanceRecord of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issued_device_type(self):
        """Gets the issued_device_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of issued device/inventory (e.g. checkbook, pay-in slip)   # noqa: E501

        :return: The issued_device_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_type

    @issued_device_type.setter
    def issued_device_type(self, issued_device_type):
        """Sets the issued_device_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of issued device/inventory (e.g. checkbook, pay-in slip)   # noqa: E501

        :param issued_device_type: The issued_device_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :type issued_device_type: str
        """

        self._issued_device_type = issued_device_type

    @property
    def issued_device_description(self):
        """Gets the issued_device_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the inventory item, including processing and handling guidelines and rules   # noqa: E501

        :return: The issued_device_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_description

    @issued_device_description.setter
    def issued_device_description(self, issued_device_description):
        """Sets the issued_device_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the inventory item, including processing and handling guidelines and rules   # noqa: E501

        :param issued_device_description: The issued_device_description of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :type issued_device_description: str
        """

        self._issued_device_description = issued_device_description

    @property
    def issued_device_option_definition(self):
        """Gets the issued_device_option_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the processing option and impact (e.g. lost check handling)   # noqa: E501

        :return: The issued_device_option_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_option_definition

    @issued_device_option_definition.setter
    def issued_device_option_definition(self, issued_device_option_definition):
        """Sets the issued_device_option_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the processing option and impact (e.g. lost check handling)   # noqa: E501

        :param issued_device_option_definition: The issued_device_option_definition of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :type issued_device_option_definition: str
        """

        self._issued_device_option_definition = issued_device_option_definition

    @property
    def issued_device_option_setting(self):
        """Gets the issued_device_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option setting    # noqa: E501

        :return: The issued_device_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :rtype: str
        """
        return self._issued_device_option_setting

    @issued_device_option_setting.setter
    def issued_device_option_setting(self, issued_device_option_setting):
        """Sets the issued_device_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The processing option setting    # noqa: E501

        :param issued_device_option_setting: The issued_device_option_setting of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :type issued_device_option_setting: str
        """

        self._issued_device_option_setting = issued_device_option_setting

    @property
    def issued_device_property(self):
        """Gets the issued_device_property of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.


        :return: The issued_device_property of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """
        return self._issued_device_property

    @issued_device_property.setter
    def issued_device_property(self, issued_device_property):
        """Sets the issued_device_property of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.


        :param issued_device_property: The issued_device_property of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecord.
        :type issued_device_property: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdIssueddeviceInitiationIssuedDeviceInstanceRecordIssuedDeviceProperty
        """

        self._issued_device_property = issued_device_property
