# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, projected_transaction_description=None, projected_transaction_fee_type=None, projected_transaction_fee_charge=None):  # noqa: E501
        """BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments - a model defined in OpenAPI

        :param projected_transaction_description: The projected_transaction_description of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.  # noqa: E501
        :type projected_transaction_description: str
        :param projected_transaction_fee_type: The projected_transaction_fee_type of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.  # noqa: E501
        :type projected_transaction_fee_type: str
        :param projected_transaction_fee_charge: The projected_transaction_fee_charge of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.  # noqa: E501
        :type projected_transaction_fee_charge: str
        """
        self.openapi_types = {
            'projected_transaction_description': str,
            'projected_transaction_fee_type': str,
            'projected_transaction_fee_charge': str
        }

        self.attribute_map = {
            'projected_transaction_description': 'projectedTransactionDescription',
            'projected_transaction_fee_type': 'projectedTransactionFeeType',
            'projected_transaction_fee_charge': 'projectedTransactionFeeCharge'
        }

        self._projected_transaction_description = projected_transaction_description
        self._projected_transaction_fee_type = projected_transaction_fee_type
        self._projected_transaction_fee_charge = projected_transaction_fee_charge

    @classmethod
    def from_dict(cls, dikt) -> 'BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQServiceFeesRetrieveOutputModel_serviceFeesInstanceRecord_feeApplicationRecord_feeProjectionsandCommitments of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.  # noqa: E501
        :rtype: BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments
        """
        return util.deserialize_model(dikt, cls)

    @property
    def projected_transaction_description(self):
        """Gets the projected_transaction_description of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: General description of the projected fee or penalty   # noqa: E501

        :return: The projected_transaction_description of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :rtype: str
        """
        return self._projected_transaction_description

    @projected_transaction_description.setter
    def projected_transaction_description(self, projected_transaction_description):
        """Sets the projected_transaction_description of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: General description of the projected fee or penalty   # noqa: E501

        :param projected_transaction_description: The projected_transaction_description of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :type projected_transaction_description: str
        """

        self._projected_transaction_description = projected_transaction_description

    @property
    def projected_transaction_fee_type(self):
        """Gets the projected_transaction_fee_type of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeTransaction.ProjectedFeeType  general-info: The fee or penalty type   # noqa: E501

        :return: The projected_transaction_fee_type of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :rtype: str
        """
        return self._projected_transaction_fee_type

    @projected_transaction_fee_type.setter
    def projected_transaction_fee_type(self, projected_transaction_fee_type):
        """Sets the projected_transaction_fee_type of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeTransaction.ProjectedFeeType  general-info: The fee or penalty type   # noqa: E501

        :param projected_transaction_fee_type: The projected_transaction_fee_type of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :type projected_transaction_fee_type: str
        """

        self._projected_transaction_fee_type = projected_transaction_fee_type

    @property
    def projected_transaction_fee_charge(self):
        """Gets the projected_transaction_fee_charge of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_FMBK98TGEeChad0JzLk7QA_-1487452687  bian-reference: FeeTransaction.ProjectedFeeAmount  general-info: The anticipated fee or penalty amount   # noqa: E501

        :return: The projected_transaction_fee_charge of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :rtype: str
        """
        return self._projected_transaction_fee_charge

    @projected_transaction_fee_charge.setter
    def projected_transaction_fee_charge(self, projected_transaction_fee_charge):
        """Sets the projected_transaction_fee_charge of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_FMBK98TGEeChad0JzLk7QA_-1487452687  bian-reference: FeeTransaction.ProjectedFeeAmount  general-info: The anticipated fee or penalty amount   # noqa: E501

        :param projected_transaction_fee_charge: The projected_transaction_fee_charge of this BQServiceFeesRetrieveOutputModelServiceFeesInstanceRecordFeeApplicationRecordFeeProjectionsandCommitments.
        :type projected_transaction_fee_charge: str
        """

        self._projected_transaction_fee_charge = projected_transaction_fee_charge
