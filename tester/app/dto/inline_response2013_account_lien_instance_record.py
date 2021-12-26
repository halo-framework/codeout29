# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class InlineResponse2013AccountLienInstanceRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lien_definition=None):  # noqa: E501
        """InlineResponse2013AccountLienInstanceRecord - a model defined in OpenAPI

        :param lien_definition: The lien_definition of this InlineResponse2013AccountLienInstanceRecord.  # noqa: E501
        :type lien_definition: str
        """
        self.openapi_types = {
            'lien_definition': str
        }

        self.attribute_map = {
            'lien_definition': 'lienDefinition'
        }

        self._lien_definition = lien_definition

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2013AccountLienInstanceRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_3_accountLienInstanceRecord of this InlineResponse2013AccountLienInstanceRecord.  # noqa: E501
        :rtype: InlineResponse2013AccountLienInstanceRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lien_definition(self):
        """Gets the lien_definition of this InlineResponse2013AccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the type of lien including processing guidelines   # noqa: E501

        :return: The lien_definition of this InlineResponse2013AccountLienInstanceRecord.
        :rtype: str
        """
        return self._lien_definition

    @lien_definition.setter
    def lien_definition(self, lien_definition):
        """Sets the lien_definition of this InlineResponse2013AccountLienInstanceRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Definition of the type of lien including processing guidelines   # noqa: E501

        :param lien_definition: The lien_definition of this InlineResponse2013AccountLienInstanceRecord.
        :type lien_definition: str
        """

        self._lien_definition = lien_definition