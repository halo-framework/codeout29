# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2006InterestInstanceRecordInterestRateConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, interest_rate_type=None, interest_rate=None):  # noqa: E501
        """InlineResponse2006InterestInstanceRecordInterestRateConfiguration - a model defined in OpenAPI

        :param interest_rate_type: The interest_rate_type of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.  # noqa: E501
        :type interest_rate_type: str
        :param interest_rate: The interest_rate of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.  # noqa: E501
        :type interest_rate: str
        """
        self.openapi_types = {
            'interest_rate_type': str,
            'interest_rate': str
        }

        self.attribute_map = {
            'interest_rate_type': 'interestRateType',
            'interest_rate': 'interestRate'
        }

        self._interest_rate_type = interest_rate_type
        self._interest_rate = interest_rate

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2006InterestInstanceRecordInterestRateConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_6_interestInstanceRecord_interestRateConfiguration of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.  # noqa: E501
        :rtype: InlineResponse2006InterestInstanceRecordInterestRateConfiguration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interest_rate_type(self):
        """Gets the interest_rate_type of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Applicable rate type   # noqa: E501

        :return: The interest_rate_type of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.
        :rtype: str
        """
        return self._interest_rate_type

    @interest_rate_type.setter
    def interest_rate_type(self, interest_rate_type):
        """Sets the interest_rate_type of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Applicable rate type   # noqa: E501

        :param interest_rate_type: The interest_rate_type of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.
        :type interest_rate_type: str
        """

        self._interest_rate_type = interest_rate_type

    @property
    def interest_rate(self):
        """Gets the interest_rate of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The rate value to be applied   # noqa: E501

        :return: The interest_rate of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The rate value to be applied   # noqa: E501

        :param interest_rate: The interest_rate of this InlineResponse2006InterestInstanceRecordInterestRateConfiguration.
        :type interest_rate: str
        """

        self._interest_rate = interest_rate
