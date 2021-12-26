# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, position_limit_settings=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits - a model defined in OpenAPI

        :param position_limit_settings: The position_limit_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :type position_limit_settings: str
        """
        self.openapi_types = {
            'position_limit_settings': str
        }

        self.attribute_map = {
            'position_limit_settings': 'positionLimitSettings'
        }

        self._position_limit_settings = position_limit_settings

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement_initiation_currentAccountFulfillmentArrangementInstanceRecord_positionLimits of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return util.deserialize_model(dikt, cls)

    @property
    def position_limit_settings(self):
        """Gets the position_limit_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The position definition, associated limit settings and rules   # noqa: E501

        :return: The position_limit_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :rtype: str
        """
        return self._position_limit_settings

    @position_limit_settings.setter
    def position_limit_settings(self, position_limit_settings):
        """Sets the position_limit_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The position definition, associated limit settings and rules   # noqa: E501

        :param position_limit_settings: The position_limit_settings of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementInitiationCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :type position_limit_settings: str
        """

        self._position_limit_settings = position_limit_settings