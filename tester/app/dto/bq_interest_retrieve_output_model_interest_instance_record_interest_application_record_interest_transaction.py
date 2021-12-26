# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transaction_description=None, transaction_rate_type=None, transaction_interest_charge=None):  # noqa: E501
        """BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction - a model defined in OpenAPI

        :param transaction_description: The transaction_description of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.  # noqa: E501
        :type transaction_description: str
        :param transaction_rate_type: The transaction_rate_type of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.  # noqa: E501
        :type transaction_rate_type: str
        :param transaction_interest_charge: The transaction_interest_charge of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.  # noqa: E501
        :type transaction_interest_charge: str
        """
        self.openapi_types = {
            'transaction_description': str,
            'transaction_rate_type': str,
            'transaction_interest_charge': str
        }

        self.attribute_map = {
            'transaction_description': 'transactionDescription',
            'transaction_rate_type': 'transactionRateType',
            'transaction_interest_charge': 'transactionInterestCharge'
        }

        self._transaction_description = transaction_description
        self._transaction_rate_type = transaction_rate_type
        self._transaction_interest_charge = transaction_interest_charge

    @classmethod
    def from_dict(cls, dikt) -> 'BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQInterestRetrieveOutputModel_interestInstanceRecord_interestApplicationRecord_interestTransaction of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.  # noqa: E501
        :rtype: BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_description(self):
        """Gets the transaction_description of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: General description of the interest transaction   # noqa: E501

        :return: The transaction_description of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :rtype: str
        """
        return self._transaction_description

    @transaction_description.setter
    def transaction_description(self, transaction_description):
        """Sets the transaction_description of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: General description of the interest transaction   # noqa: E501

        :param transaction_description: The transaction_description of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :type transaction_description: str
        """

        self._transaction_description = transaction_description

    @property
    def transaction_rate_type(self):
        """Gets the transaction_rate_type of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5P_9MTGEeChad0JzLk7QA_218224835/elements/_2b6L4A4hEeO3g-FNSwkb-g_-1305263591  bian-reference: InterestTransaction.AppliedInterestType  general-info: Applicable rate type   # noqa: E501

        :return: The transaction_rate_type of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :rtype: str
        """
        return self._transaction_rate_type

    @transaction_rate_type.setter
    def transaction_rate_type(self, transaction_rate_type):
        """Sets the transaction_rate_type of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5P_9MTGEeChad0JzLk7QA_218224835/elements/_2b6L4A4hEeO3g-FNSwkb-g_-1305263591  bian-reference: InterestTransaction.AppliedInterestType  general-info: Applicable rate type   # noqa: E501

        :param transaction_rate_type: The transaction_rate_type of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :type transaction_rate_type: str
        """

        self._transaction_rate_type = transaction_rate_type

    @property
    def transaction_interest_charge(self):
        """Gets the transaction_interest_charge of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5P_9MTGEeChad0JzLk7QA_218224835/elements/_E5P_98TGEeChad0JzLk7QA_2006810136  bian-reference: InterestTransaction.AppliedInterestAmount  general-info: The derived interest amount to be applied   # noqa: E501

        :return: The transaction_interest_charge of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :rtype: str
        """
        return self._transaction_interest_charge

    @transaction_interest_charge.setter
    def transaction_interest_charge(self, transaction_interest_charge):
        """Sets the transaction_interest_charge of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_E5P_9MTGEeChad0JzLk7QA_218224835/elements/_E5P_98TGEeChad0JzLk7QA_2006810136  bian-reference: InterestTransaction.AppliedInterestAmount  general-info: The derived interest amount to be applied   # noqa: E501

        :param transaction_interest_charge: The transaction_interest_charge of this BQInterestRetrieveOutputModelInterestInstanceRecordInterestApplicationRecordInterestTransaction.
        :type transaction_interest_charge: str
        """

        self._transaction_interest_charge = transaction_interest_charge
