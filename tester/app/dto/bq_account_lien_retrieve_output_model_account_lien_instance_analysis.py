# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_lien_instance_analysis_record=None, account_lien_instance_analysis_report_type=None, account_lien_instance_analysis_parameters=None, account_lien_instance_analysis_report=None):  # noqa: E501
        """BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis - a model defined in OpenAPI

        :param account_lien_instance_analysis_record: The account_lien_instance_analysis_record of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.  # noqa: E501
        :type account_lien_instance_analysis_record: object
        :param account_lien_instance_analysis_report_type: The account_lien_instance_analysis_report_type of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.  # noqa: E501
        :type account_lien_instance_analysis_report_type: str
        :param account_lien_instance_analysis_parameters: The account_lien_instance_analysis_parameters of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.  # noqa: E501
        :type account_lien_instance_analysis_parameters: str
        :param account_lien_instance_analysis_report: The account_lien_instance_analysis_report of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.  # noqa: E501
        :type account_lien_instance_analysis_report: object
        """
        self.openapi_types = {
            'account_lien_instance_analysis_record': object,
            'account_lien_instance_analysis_report_type': str,
            'account_lien_instance_analysis_parameters': str,
            'account_lien_instance_analysis_report': object
        }

        self.attribute_map = {
            'account_lien_instance_analysis_record': 'accountLienInstanceAnalysisRecord',
            'account_lien_instance_analysis_report_type': 'accountLienInstanceAnalysisReportType',
            'account_lien_instance_analysis_parameters': 'accountLienInstanceAnalysisParameters',
            'account_lien_instance_analysis_report': 'accountLienInstanceAnalysisReport'
        }

        self._account_lien_instance_analysis_record = account_lien_instance_analysis_record
        self._account_lien_instance_analysis_report_type = account_lien_instance_analysis_report_type
        self._account_lien_instance_analysis_parameters = account_lien_instance_analysis_parameters
        self._account_lien_instance_analysis_report = account_lien_instance_analysis_report

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountLienRetrieveOutputModel_accountLienInstanceAnalysis of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.  # noqa: E501
        :rtype: BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_lien_instance_analysis_record(self):
        """Gets the account_lien_instance_analysis_record of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :return: The account_lien_instance_analysis_record of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :rtype: object
        """
        return self._account_lien_instance_analysis_record

    @account_lien_instance_analysis_record.setter
    def account_lien_instance_analysis_record(self, account_lien_instance_analysis_record):
        """Sets the account_lien_instance_analysis_record of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The inputs and results of the instance analysis that can be on-going, periodic and actual and projected   # noqa: E501

        :param account_lien_instance_analysis_record: The account_lien_instance_analysis_record of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :type account_lien_instance_analysis_record: object
        """

        self._account_lien_instance_analysis_record = account_lien_instance_analysis_record

    @property
    def account_lien_instance_analysis_report_type(self):
        """Gets the account_lien_instance_analysis_report_type of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :return: The account_lien_instance_analysis_report_type of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :rtype: str
        """
        return self._account_lien_instance_analysis_report_type

    @account_lien_instance_analysis_report_type.setter
    def account_lien_instance_analysis_report_type(self, account_lien_instance_analysis_report_type):
        """Sets the account_lien_instance_analysis_report_type of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Code  general-info: The type of external performance analysis report available   # noqa: E501

        :param account_lien_instance_analysis_report_type: The account_lien_instance_analysis_report_type of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :type account_lien_instance_analysis_report_type: str
        """

        self._account_lien_instance_analysis_report_type = account_lien_instance_analysis_report_type

    @property
    def account_lien_instance_analysis_parameters(self):
        """Gets the account_lien_instance_analysis_parameters of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :return: The account_lien_instance_analysis_parameters of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :rtype: str
        """
        return self._account_lien_instance_analysis_parameters

    @account_lien_instance_analysis_parameters.setter
    def account_lien_instance_analysis_parameters(self, account_lien_instance_analysis_parameters):
        """Sets the account_lien_instance_analysis_parameters of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The selection parameters for the analysis (e.g. period, algorithm type)   # noqa: E501

        :param account_lien_instance_analysis_parameters: The account_lien_instance_analysis_parameters of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :type account_lien_instance_analysis_parameters: str
        """

        self._account_lien_instance_analysis_parameters = account_lien_instance_analysis_parameters

    @property
    def account_lien_instance_analysis_report(self):
        """Gets the account_lien_instance_analysis_report of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :return: The account_lien_instance_analysis_report of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :rtype: object
        """
        return self._account_lien_instance_analysis_report

    @account_lien_instance_analysis_report.setter
    def account_lien_instance_analysis_report(self, account_lien_instance_analysis_report):
        """Sets the account_lien_instance_analysis_report of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Binary  general-info: The external analysis report in any suitable form including selection filters where appropriate   # noqa: E501

        :param account_lien_instance_analysis_report: The account_lien_instance_analysis_report of this BQAccountLienRetrieveOutputModelAccountLienInstanceAnalysis.
        :type account_lien_instance_analysis_report: object
        """

        self._account_lien_instance_analysis_report = account_lien_instance_analysis_report
