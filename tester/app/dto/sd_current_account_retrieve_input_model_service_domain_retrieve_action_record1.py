# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_control_record_portfolio_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_service_domain_activity_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_service_domain_performance_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis
from tester import util

from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_control_record_portfolio_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis  # noqa: E501
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_service_domain_activity_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis  # noqa: E501
from tester.app.dto.sd_current_account_retrieve_input_model_service_domain_retrieve_action_record1_service_domain_performance_analysis import SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis  # noqa: E501



class SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_domain_activity_analysis=None, service_domain_performance_analysis=None, control_record_portfolio_analysis=None):  # noqa: E501
        """SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1 - a model defined in OpenAPI

        :param service_domain_activity_analysis: The service_domain_activity_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.  # noqa: E501
        :type service_domain_activity_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis
        :param service_domain_performance_analysis: The service_domain_performance_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.  # noqa: E501
        :type service_domain_performance_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis
        :param control_record_portfolio_analysis: The control_record_portfolio_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.  # noqa: E501
        :type control_record_portfolio_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis
        """
        self.openapi_types = {
            'service_domain_activity_analysis': SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis,
            'service_domain_performance_analysis': SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis,
            'control_record_portfolio_analysis': SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis
        }

        self.attribute_map = {
            'service_domain_activity_analysis': 'serviceDomainActivityAnalysis',
            'service_domain_performance_analysis': 'serviceDomainPerformanceAnalysis',
            'control_record_portfolio_analysis': 'controlRecordPortfolioAnalysis'
        }

        self._service_domain_activity_analysis = service_domain_activity_analysis
        self._service_domain_performance_analysis = service_domain_performance_analysis
        self._control_record_portfolio_analysis = control_record_portfolio_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SDCurrentAccountRetrieveInputModel_serviceDomainRetrieveActionRecord_1 of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.  # noqa: E501
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_domain_activity_analysis(self):
        """Gets the service_domain_activity_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :return: The service_domain_activity_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis
        """
        return self._service_domain_activity_analysis

    @service_domain_activity_analysis.setter
    def service_domain_activity_analysis(self, service_domain_activity_analysis):
        """Sets the service_domain_activity_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :param service_domain_activity_analysis: The service_domain_activity_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :type service_domain_activity_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainActivityAnalysis
        """

        self._service_domain_activity_analysis = service_domain_activity_analysis

    @property
    def service_domain_performance_analysis(self):
        """Gets the service_domain_performance_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :return: The service_domain_performance_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis
        """
        return self._service_domain_performance_analysis

    @service_domain_performance_analysis.setter
    def service_domain_performance_analysis(self, service_domain_performance_analysis):
        """Sets the service_domain_performance_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :param service_domain_performance_analysis: The service_domain_performance_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :type service_domain_performance_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ServiceDomainPerformanceAnalysis
        """

        self._service_domain_performance_analysis = service_domain_performance_analysis

    @property
    def control_record_portfolio_analysis(self):
        """Gets the control_record_portfolio_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :return: The control_record_portfolio_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :rtype: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis
        """
        return self._control_record_portfolio_analysis

    @control_record_portfolio_analysis.setter
    def control_record_portfolio_analysis(self, control_record_portfolio_analysis):
        """Sets the control_record_portfolio_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.


        :param control_record_portfolio_analysis: The control_record_portfolio_analysis of this SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1.
        :type control_record_portfolio_analysis: SDCurrentAccountRetrieveInputModelServiceDomainRetrieveActionRecord1ControlRecordPortfolioAnalysis
        """

        self._control_record_portfolio_analysis = control_record_portfolio_analysis
