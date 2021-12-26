# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fee_type=None):  # noqa: E501
        """CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile - a model defined in OpenAPI

        :param fee_type: The fee_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.  # noqa: E501
        :type fee_type: str
        """
        self.openapi_types = {
            'fee_type': str
        }

        self.attribute_map = {
            'fee_type': 'feeType'
        }

        self._fee_type = fee_type

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _current_account__sd_reference_id__current_account_fulfillment_arrangement__cr_reference_id__servicefees_initiation_serviceFeesInstanceRecord_feeConfigurationProfile of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.  # noqa: E501
        :rtype: CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fee_type(self):
        """Gets the fee_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeFeature.FeeType `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeFeature.FeeType  general-info: The fee or penalty type applied   # noqa: E501

        :return: The fee_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.
        :rtype: str
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeFeature.FeeType `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeFeature.FeeType  general-info: The fee or penalty type applied   # noqa: E501

        :param fee_type: The fee_type of this CurrentAccountSdReferenceIdCurrentAccountFulfillmentArrangementCrReferenceIdServicefeesInitiationServiceFeesInstanceRecordFeeConfigurationProfile.
        :type fee_type: str
        """

        self._fee_type = fee_type