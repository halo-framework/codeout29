# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, position_limit_settings=None, position_limit_value=None):  # noqa: E501
        """InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits - a model defined in OpenAPI

        :param position_limit_settings: The position_limit_settings of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :type position_limit_settings: str
        :param position_limit_value: The position_limit_value of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :type position_limit_value: str
        """
        self.openapi_types = {
            'position_limit_settings': str,
            'position_limit_value': str
        }

        self.attribute_map = {
            'position_limit_settings': 'positionLimitSettings',
            'position_limit_value': 'positionLimitValue'
        }

        self._position_limit_settings = position_limit_settings
        self._position_limit_value = position_limit_value

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_3_currentAccountFulfillmentArrangementInstanceRecord_positionLimits of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :rtype: InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return util.deserialize_model(dikt, cls)

    @property
    def position_limit_settings(self):
        """Gets the position_limit_settings of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The position definition, associated limit settings and rules   # noqa: E501

        :return: The position_limit_settings of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :rtype: str
        """
        return self._position_limit_settings

    @position_limit_settings.setter
    def position_limit_settings(self, position_limit_settings):
        """Sets the position_limit_settings of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The position definition, associated limit settings and rules   # noqa: E501

        :param position_limit_settings: The position_limit_settings of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :type position_limit_settings: str
        """

        self._position_limit_settings = position_limit_settings

    @property
    def position_limit_value(self):
        """Gets the position_limit_value of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The current calculated position   # noqa: E501

        :return: The position_limit_value of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :rtype: str
        """
        return self._position_limit_value

    @position_limit_value.setter
    def position_limit_value(self, position_limit_value):
        """Sets the position_limit_value of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The current calculated position   # noqa: E501

        :param position_limit_value: The position_limit_value of this InlineResponse2013CurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :type position_limit_value: str
        """

        self._position_limit_value = position_limit_value
