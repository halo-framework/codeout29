# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.bq_account_lien_retrieve_input_model_account_lien_instance_analysis1 import BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1
from tester.app.dto.bq_account_lien_retrieve_input_model_account_lien_instance_report1 import BQAccountLienRetrieveInputModelAccountLienInstanceReport1
from tester import util

from tester.app.dto.bq_account_lien_retrieve_input_model_account_lien_instance_analysis1 import BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1  # noqa: E501
from tester.app.dto.bq_account_lien_retrieve_input_model_account_lien_instance_report1 import BQAccountLienRetrieveInputModelAccountLienInstanceReport1  # noqa: E501



class BQAccountLienRetrieveInputModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_lien_retrieve_action_task_record=None, account_lien_retrieve_action_request=None, account_lien_instance_report=None, account_lien_instance_analysis=None):  # noqa: E501
        """BQAccountLienRetrieveInputModel - a model defined in OpenAPI

        :param account_lien_retrieve_action_task_record: The account_lien_retrieve_action_task_record of this BQAccountLienRetrieveInputModel.  # noqa: E501
        :type account_lien_retrieve_action_task_record: object
        :param account_lien_retrieve_action_request: The account_lien_retrieve_action_request of this BQAccountLienRetrieveInputModel.  # noqa: E501
        :type account_lien_retrieve_action_request: str
        :param account_lien_instance_report: The account_lien_instance_report of this BQAccountLienRetrieveInputModel.  # noqa: E501
        :type account_lien_instance_report: BQAccountLienRetrieveInputModelAccountLienInstanceReport1
        :param account_lien_instance_analysis: The account_lien_instance_analysis of this BQAccountLienRetrieveInputModel.  # noqa: E501
        :type account_lien_instance_analysis: BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1
        """
        self.openapi_types = {
            'account_lien_retrieve_action_task_record': object,
            'account_lien_retrieve_action_request': str,
            'account_lien_instance_report': BQAccountLienRetrieveInputModelAccountLienInstanceReport1,
            'account_lien_instance_analysis': BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1
        }

        self.attribute_map = {
            'account_lien_retrieve_action_task_record': 'accountLienRetrieveActionTaskRecord',
            'account_lien_retrieve_action_request': 'accountLienRetrieveActionRequest',
            'account_lien_instance_report': 'accountLienInstanceReport',
            'account_lien_instance_analysis': 'accountLienInstanceAnalysis'
        }

        self._account_lien_retrieve_action_task_record = account_lien_retrieve_action_task_record
        self._account_lien_retrieve_action_request = account_lien_retrieve_action_request
        self._account_lien_instance_report = account_lien_instance_report
        self._account_lien_instance_analysis = account_lien_instance_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountLienRetrieveInputModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountLienRetrieveInputModel of this BQAccountLienRetrieveInputModel.  # noqa: E501
        :rtype: BQAccountLienRetrieveInputModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_lien_retrieve_action_task_record(self):
        """Gets the account_lien_retrieve_action_task_record of this BQAccountLienRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :return: The account_lien_retrieve_action_task_record of this BQAccountLienRetrieveInputModel.
        :rtype: object
        """
        return self._account_lien_retrieve_action_task_record

    @account_lien_retrieve_action_task_record.setter
    def account_lien_retrieve_action_task_record(self, account_lien_retrieve_action_task_record):
        """Sets the account_lien_retrieve_action_task_record of this BQAccountLienRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The retrieve service call consolidated processing record   # noqa: E501

        :param account_lien_retrieve_action_task_record: The account_lien_retrieve_action_task_record of this BQAccountLienRetrieveInputModel.
        :type account_lien_retrieve_action_task_record: object
        """

        self._account_lien_retrieve_action_task_record = account_lien_retrieve_action_task_record

    @property
    def account_lien_retrieve_action_request(self):
        """Gets the account_lien_retrieve_action_request of this BQAccountLienRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service request (lists requested reports)   # noqa: E501

        :return: The account_lien_retrieve_action_request of this BQAccountLienRetrieveInputModel.
        :rtype: str
        """
        return self._account_lien_retrieve_action_request

    @account_lien_retrieve_action_request.setter
    def account_lien_retrieve_action_request(self, account_lien_retrieve_action_request):
        """Sets the account_lien_retrieve_action_request of this BQAccountLienRetrieveInputModel.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Details of the retrieve action service request (lists requested reports)   # noqa: E501

        :param account_lien_retrieve_action_request: The account_lien_retrieve_action_request of this BQAccountLienRetrieveInputModel.
        :type account_lien_retrieve_action_request: str
        """

        self._account_lien_retrieve_action_request = account_lien_retrieve_action_request

    @property
    def account_lien_instance_report(self):
        """Gets the account_lien_instance_report of this BQAccountLienRetrieveInputModel.


        :return: The account_lien_instance_report of this BQAccountLienRetrieveInputModel.
        :rtype: BQAccountLienRetrieveInputModelAccountLienInstanceReport1
        """
        return self._account_lien_instance_report

    @account_lien_instance_report.setter
    def account_lien_instance_report(self, account_lien_instance_report):
        """Sets the account_lien_instance_report of this BQAccountLienRetrieveInputModel.


        :param account_lien_instance_report: The account_lien_instance_report of this BQAccountLienRetrieveInputModel.
        :type account_lien_instance_report: BQAccountLienRetrieveInputModelAccountLienInstanceReport1
        """

        self._account_lien_instance_report = account_lien_instance_report

    @property
    def account_lien_instance_analysis(self):
        """Gets the account_lien_instance_analysis of this BQAccountLienRetrieveInputModel.


        :return: The account_lien_instance_analysis of this BQAccountLienRetrieveInputModel.
        :rtype: BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1
        """
        return self._account_lien_instance_analysis

    @account_lien_instance_analysis.setter
    def account_lien_instance_analysis(self, account_lien_instance_analysis):
        """Sets the account_lien_instance_analysis of this BQAccountLienRetrieveInputModel.


        :param account_lien_instance_analysis: The account_lien_instance_analysis of this BQAccountLienRetrieveInputModel.
        :type account_lien_instance_analysis: BQAccountLienRetrieveInputModelAccountLienInstanceAnalysis1
        """

        self._account_lien_instance_analysis = account_lien_instance_analysis