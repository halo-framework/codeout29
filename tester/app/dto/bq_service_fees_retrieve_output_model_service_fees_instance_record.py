# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.inline_response2008_service_fees_instance_record_fee_application_record import InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord
from tester.app.dto.inline_response2008_service_fees_instance_record_fee_configuration_profile import InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile
from tester import util

from tester.app.dto.inline_response2008_service_fees_instance_record_fee_application_record import InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord  # noqa: E501
from tester.app.dto.inline_response2008_service_fees_instance_record_fee_configuration_profile import InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile  # noqa: E501



class BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fee_configuration_profile=None, fee_application_record=None):  # noqa: E501
        """BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord - a model defined in OpenAPI

        :param fee_configuration_profile: The fee_configuration_profile of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.  # noqa: E501
        :type fee_configuration_profile: InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile
        :param fee_application_record: The fee_application_record of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.  # noqa: E501
        :type fee_application_record: InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord
        """
        self.openapi_types = {
            'fee_configuration_profile': InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile,
            'fee_application_record': InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord
        }

        self.attribute_map = {
            'fee_configuration_profile': 'feeConfigurationProfile',
            'fee_application_record': 'feeApplicationRecord'
        }

        self._fee_configuration_profile = fee_configuration_profile
        self._fee_application_record = fee_application_record

    @classmethod
    def from_dict(cls, dikt) -> 'BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQServiceFeesRetrieveOutputModel_serviceFeesInstanceRecord of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.  # noqa: E501
        :rtype: BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fee_configuration_profile(self):
        """Gets the fee_configuration_profile of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.


        :return: The fee_configuration_profile of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.
        :rtype: InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile
        """
        return self._fee_configuration_profile

    @fee_configuration_profile.setter
    def fee_configuration_profile(self, fee_configuration_profile):
        """Sets the fee_configuration_profile of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.


        :param fee_configuration_profile: The fee_configuration_profile of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.
        :type fee_configuration_profile: InlineResponse2008ServiceFeesInstanceRecordFeeConfigurationProfile
        """

        self._fee_configuration_profile = fee_configuration_profile

    @property
    def fee_application_record(self):
        """Gets the fee_application_record of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.


        :return: The fee_application_record of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.
        :rtype: InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord
        """
        return self._fee_application_record

    @fee_application_record.setter
    def fee_application_record(self, fee_application_record):
        """Sets the fee_application_record of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.


        :param fee_application_record: The fee_application_record of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecord.
        :type fee_application_record: InlineResponse2008ServiceFeesInstanceRecordFeeApplicationRecord
        """

        self._fee_application_record = fee_application_record
