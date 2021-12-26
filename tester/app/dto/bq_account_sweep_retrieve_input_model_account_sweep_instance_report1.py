# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_sweep_instance_report_reference=None):  # noqa: E501
        """BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1 - a model defined in OpenAPI

        :param account_sweep_instance_report_reference: The account_sweep_instance_report_reference of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.  # noqa: E501
        :type account_sweep_instance_report_reference: str
        """
        self.openapi_types = {
            'account_sweep_instance_report_reference': str
        }

        self.attribute_map = {
            'account_sweep_instance_report_reference': 'accountSweepInstanceReportReference'
        }

        self._account_sweep_instance_report_reference = account_sweep_instance_report_reference

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountSweepRetrieveInputModel_accountSweepInstanceReport_1 of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.  # noqa: E501
        :rtype: BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_sweep_instance_report_reference(self):
        """Gets the account_sweep_instance_report_reference of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance report   # noqa: E501

        :return: The account_sweep_instance_report_reference of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.
        :rtype: str
        """
        return self._account_sweep_instance_report_reference

    @account_sweep_instance_report_reference.setter
    def account_sweep_instance_report_reference(self, account_sweep_instance_report_reference):
        """Sets the account_sweep_instance_report_reference of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::ISO20022andUNCEFACT::Identifier  general-info: Reference to the control record instance report   # noqa: E501

        :param account_sweep_instance_report_reference: The account_sweep_instance_report_reference of this BQAccountSweepRetrieveInputModelAccountSweepInstanceReport1.
        :type account_sweep_instance_report_reference: str
        """

        self._account_sweep_instance_report_reference = account_sweep_instance_report_reference
