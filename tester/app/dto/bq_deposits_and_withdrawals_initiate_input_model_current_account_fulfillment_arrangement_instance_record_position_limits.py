# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, position_limit_type=None):  # noqa: E501
        """BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits - a model defined in OpenAPI

        :param position_limit_type: The position_limit_type of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :type position_limit_type: str
        """
        self.openapi_types = {
            'position_limit_type': str
        }

        self.attribute_map = {
            'position_limit_type': 'positionLimitType'
        }

        self._position_limit_type = position_limit_type

    @classmethod
    def from_dict(cls, dikt) -> 'BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQDepositsAndWithdrawalsInitiateInputModel_currentAccountFulfillmentArrangementInstanceRecord_positionLimits of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.  # noqa: E501
        :rtype: BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits
        """
        return util.deserialize_model(dikt, cls)

    @property
    def position_limit_type(self):
        """Gets the position_limit_type of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of position maintained for the account (e.g. transaction credit/debit, netting, position)   # noqa: E501

        :return: The position_limit_type of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :rtype: str
        """
        return self._position_limit_type

    @position_limit_type.setter
    def position_limit_type(self, position_limit_type):
        """Sets the position_limit_type of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The type of position maintained for the account (e.g. transaction credit/debit, netting, position)   # noqa: E501

        :param position_limit_type: The position_limit_type of this BQDepositsAndWithdrawalsInitiateInputModelCurrentAccountFulfillmentArrangementInstanceRecordPositionLimits.
        :type position_limit_type: str
        """

        self._position_limit_type = position_limit_type
