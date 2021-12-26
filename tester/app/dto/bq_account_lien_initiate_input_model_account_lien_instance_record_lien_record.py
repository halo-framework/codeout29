# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lien_originator=None, lien_purpose=None, lien_amount=None, lien_start_date=None, lien_expiry_date=None, lien_status=None):  # noqa: E501
        """BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord - a model defined in OpenAPI

        :param lien_originator: The lien_originator of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_originator: str
        :param lien_purpose: The lien_purpose of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_purpose: str
        :param lien_amount: The lien_amount of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_amount: str
        :param lien_start_date: The lien_start_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_start_date: str
        :param lien_expiry_date: The lien_expiry_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_expiry_date: str
        :param lien_status: The lien_status of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :type lien_status: str
        """
        self.openapi_types = {
            'lien_originator': str,
            'lien_purpose': str,
            'lien_amount': str,
            'lien_start_date': str,
            'lien_expiry_date': str,
            'lien_status': str
        }

        self.attribute_map = {
            'lien_originator': 'lienOriginator',
            'lien_purpose': 'lienPurpose',
            'lien_amount': 'lienAmount',
            'lien_start_date': 'lienStartDate',
            'lien_expiry_date': 'lienExpiryDate',
            'lien_status': 'lienStatus'
        }

        self._lien_originator = lien_originator
        self._lien_purpose = lien_purpose
        self._lien_amount = lien_amount
        self._lien_start_date = lien_start_date
        self._lien_expiry_date = lien_expiry_date
        self._lien_status = lien_status

    @classmethod
    def from_dict(cls, dikt) -> 'BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQAccountLienInitiateInputModel_accountLienInstanceRecord_lienRecord of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.  # noqa: E501
        :rtype: BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lien_originator(self):
        """Gets the lien_originator of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The party requesting the lien   # noqa: E501

        :return: The lien_originator of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_originator

    @lien_originator.setter
    def lien_originator(self, lien_originator):
        """Sets the lien_originator of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The party requesting the lien   # noqa: E501

        :param lien_originator: The lien_originator of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_originator: str
        """

        self._lien_originator = lien_originator

    @property
    def lien_purpose(self):
        """Gets the lien_purpose of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The purpose or associated facility linked to the lien   # noqa: E501

        :return: The lien_purpose of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_purpose

    @lien_purpose.setter
    def lien_purpose(self, lien_purpose):
        """Sets the lien_purpose of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The purpose or associated facility linked to the lien   # noqa: E501

        :param lien_purpose: The lien_purpose of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_purpose: str
        """

        self._lien_purpose = lien_purpose

    @property
    def lien_amount(self):
        """Gets the lien_amount of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The amount being blocked   # noqa: E501

        :return: The lien_amount of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_amount

    @lien_amount.setter
    def lien_amount(self, lien_amount):
        """Sets the lien_amount of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Amount  general-info: The amount being blocked   # noqa: E501

        :param lien_amount: The lien_amount of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_amount: str
        """

        self._lien_amount = lien_amount

    @property
    def lien_start_date(self):
        """Gets the lien_start_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date the lien is enforced   # noqa: E501

        :return: The lien_start_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_start_date

    @lien_start_date.setter
    def lien_start_date(self, lien_start_date):
        """Sets the lien_start_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date the lien is enforced   # noqa: E501

        :param lien_start_date: The lien_start_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_start_date: str
        """

        self._lien_start_date = lien_start_date

    @property
    def lien_expiry_date(self):
        """Gets the lien_expiry_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date the lien is removed   # noqa: E501

        :return: The lien_expiry_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_expiry_date

    @lien_expiry_date.setter
    def lien_expiry_date(self, lien_expiry_date):
        """Sets the lien_expiry_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::DateTime  general-info: The date the lien is removed   # noqa: E501

        :param lien_expiry_date: The lien_expiry_date of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_expiry_date: str
        """

        self._lien_expiry_date = lien_expiry_date

    @property
    def lien_status(self):
        """Gets the lien_status of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status on the lien   # noqa: E501

        :return: The lien_status of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :rtype: str
        """
        return self._lien_status

    @lien_status.setter
    def lien_status(self, lien_status):
        """Sets the lien_status of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: The status on the lien   # noqa: E501

        :param lien_status: The lien_status of this BQAccountLienInitiateInputModelAccountLienInstanceRecordLienRecord.
        :type lien_status: str
        """

        self._lien_status = lien_status
