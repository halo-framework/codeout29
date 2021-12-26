# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_position_limits import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
from tester.app.dto.inline_response2017_current_account_fulfillment_arrangement_instance_record_associations import InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations
from tester import util

from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_date_type import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType  # noqa: E501
from tester.app.dto.current_account_sd_reference_id_current_account_fulfillment_arrangement_initiation_current_account_fulfillment_arrangement_instance_record_position_limits import CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits  # noqa: E501
from tester.app.dto.inline_response2017_current_account_fulfillment_arrangement_instance_record_associations import InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations  # noqa: E501



class BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, associations=None, position_limits=None, date_type=None):  # noqa: E501
        """BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord - a model defined in OpenAPI

        :param associations: The associations of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type associations: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations
        :param position_limits: The position_limits of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type position_limits: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        :param date_type: The date_type of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        self.openapi_types = {
            'associations': InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations,
            'position_limits': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits,
            'date_type': CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        }

        self.attribute_map = {
            'associations': 'associations',
            'position_limits': 'positionLimits',
            'date_type': 'dateType'
        }

        self._associations = associations
        self._position_limits = position_limits
        self._date_type = date_type

    @classmethod
    def from_dict(cls, dikt) -> 'BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQIssuedDeviceInitiateOutputModel_currentAccountFulfillmentArrangementInstanceRecord of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.  # noqa: E501
        :rtype: BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associations(self):
        """Gets the associations of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The associations of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param associations: The associations of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type associations: InlineResponse2017CurrentAccountFulfillmentArrangementInstanceRecordAssociations
        """

        self._associations = associations

    @property
    def position_limits(self):
        """Gets the position_limits of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The position_limits of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return self._position_limits

    @position_limits.setter
    def position_limits(self, position_limits):
        """Sets the position_limits of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param position_limits: The position_limits of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type position_limits: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """

        self._position_limits = position_limits

    @property
    def date_type(self):
        """Gets the date_type of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :return: The date_type of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.


        :param date_type: The date_type of this BQIssuedDeviceInitiateOutputModelCurrentAccountFulfillmentArrangementInstanceRecord.
        :type date_type: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordDateType
        """

        self._date_type = date_type