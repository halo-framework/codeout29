# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tester.app.dto.base_model_ import Model
from tester import util




class BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, payment_transaction_type=None, payment_transaction_payee_reference=None, payment_transaction_payee_account_reference=None, payment_transaction_payee_bank_reference=None, payment_transaction_amount=None, payment_transaction_fee_type=None, payment_transaction_fee_charge=None, payment_transaction_date=None, payment_transaction_payment_mechanism=None, payment_transaction_payment_purpose=None, payment_transaction_bank_branch_location_reference=None, payment_transaction_status=None):  # noqa: E501
        """BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction - a model defined in OpenAPI

        :param payment_transaction_type: The payment_transaction_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_type: str
        :param payment_transaction_payee_reference: The payment_transaction_payee_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_payee_reference: str
        :param payment_transaction_payee_account_reference: The payment_transaction_payee_account_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_payee_account_reference: str
        :param payment_transaction_payee_bank_reference: The payment_transaction_payee_bank_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_payee_bank_reference: str
        :param payment_transaction_amount: The payment_transaction_amount of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_amount: str
        :param payment_transaction_fee_type: The payment_transaction_fee_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_fee_type: str
        :param payment_transaction_fee_charge: The payment_transaction_fee_charge of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_fee_charge: str
        :param payment_transaction_date: The payment_transaction_date of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_date: str
        :param payment_transaction_payment_mechanism: The payment_transaction_payment_mechanism of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_payment_mechanism: str
        :param payment_transaction_payment_purpose: The payment_transaction_payment_purpose of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_payment_purpose: str
        :param payment_transaction_bank_branch_location_reference: The payment_transaction_bank_branch_location_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_bank_branch_location_reference: str
        :param payment_transaction_status: The payment_transaction_status of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :type payment_transaction_status: str
        """
        self.openapi_types = {
            'payment_transaction_type': str,
            'payment_transaction_payee_reference': str,
            'payment_transaction_payee_account_reference': str,
            'payment_transaction_payee_bank_reference': str,
            'payment_transaction_amount': str,
            'payment_transaction_fee_type': str,
            'payment_transaction_fee_charge': str,
            'payment_transaction_date': str,
            'payment_transaction_payment_mechanism': str,
            'payment_transaction_payment_purpose': str,
            'payment_transaction_bank_branch_location_reference': str,
            'payment_transaction_status': str
        }

        self.attribute_map = {
            'payment_transaction_type': 'paymentTransactionType',
            'payment_transaction_payee_reference': 'paymentTransactionPayeeReference',
            'payment_transaction_payee_account_reference': 'paymentTransactionPayeeAccountReference',
            'payment_transaction_payee_bank_reference': 'paymentTransactionPayeeBankReference',
            'payment_transaction_amount': 'paymentTransactionAmount',
            'payment_transaction_fee_type': 'paymentTransactionFeeType',
            'payment_transaction_fee_charge': 'paymentTransactionFeeCharge',
            'payment_transaction_date': 'paymentTransactionDate',
            'payment_transaction_payment_mechanism': 'paymentTransactionPaymentMechanism',
            'payment_transaction_payment_purpose': 'paymentTransactionPaymentPurpose',
            'payment_transaction_bank_branch_location_reference': 'paymentTransactionBankBranchLocationReference',
            'payment_transaction_status': 'paymentTransactionStatus'
        }

        self._payment_transaction_type = payment_transaction_type
        self._payment_transaction_payee_reference = payment_transaction_payee_reference
        self._payment_transaction_payee_account_reference = payment_transaction_payee_account_reference
        self._payment_transaction_payee_bank_reference = payment_transaction_payee_bank_reference
        self._payment_transaction_amount = payment_transaction_amount
        self._payment_transaction_fee_type = payment_transaction_fee_type
        self._payment_transaction_fee_charge = payment_transaction_fee_charge
        self._payment_transaction_date = payment_transaction_date
        self._payment_transaction_payment_mechanism = payment_transaction_payment_mechanism
        self._payment_transaction_payment_purpose = payment_transaction_payment_purpose
        self._payment_transaction_bank_branch_location_reference = payment_transaction_bank_branch_location_reference
        self._payment_transaction_status = payment_transaction_status

    @classmethod
    def from_dict(cls, dikt) -> 'BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BQPaymentsRetrieveOutputModel_paymentsInstanceRecord_paymentTransaction of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.  # noqa: E501
        :rtype: BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def payment_transaction_type(self):
        """Gets the payment_transaction_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FA2cwMTGEeChad0JzLk7QA_1385452657/elements/_q58kEK23EeKuGrOch6U_ZQ_-1354685933  bian-reference: PaymentTransactionType  general-info: The type of payment transaction (e.g. customer payment, standing order, direct debit, bill pay)   # noqa: E501

        :return: The payment_transaction_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_type

    @payment_transaction_type.setter
    def payment_transaction_type(self, payment_transaction_type):
        """Sets the payment_transaction_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FA2cwMTGEeChad0JzLk7QA_1385452657/elements/_q58kEK23EeKuGrOch6U_ZQ_-1354685933  bian-reference: PaymentTransactionType  general-info: The type of payment transaction (e.g. customer payment, standing order, direct debit, bill pay)   # noqa: E501

        :param payment_transaction_type: The payment_transaction_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_type: str
        """

        self._payment_transaction_type = payment_transaction_type

    @property
    def payment_transaction_payee_reference(self):
        """Gets the payment_transaction_payee_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EteNycTGEeChad0JzLk7QA_-591715083  bian-reference: PaymentTransactionInvolvementType (as Payee)  general-info: Reference to the party to whom the payment is made   # noqa: E501

        :return: The payment_transaction_payee_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_payee_reference

    @payment_transaction_payee_reference.setter
    def payment_transaction_payee_reference(self, payment_transaction_payee_reference):
        """Sets the payment_transaction_payee_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EteNycTGEeChad0JzLk7QA_-591715083  bian-reference: PaymentTransactionInvolvementType (as Payee)  general-info: Reference to the party to whom the payment is made   # noqa: E501

        :param payment_transaction_payee_reference: The payment_transaction_payee_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_payee_reference: str
        """

        self._payment_transaction_payee_reference = payment_transaction_payee_reference

    @property
    def payment_transaction_payee_account_reference(self):
        """Gets the payment_transaction_payee_account_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_4a7goJo3EeOJb4DIsGFWTA  bian-reference: PaymentTransaction.Account (as Payee Account)  general-info: Reference to the account to which the payment is made   # noqa: E501

        :return: The payment_transaction_payee_account_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_payee_account_reference

    @payment_transaction_payee_account_reference.setter
    def payment_transaction_payee_account_reference(self, payment_transaction_payee_account_reference):
        """Sets the payment_transaction_payee_account_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_4a7goJo3EeOJb4DIsGFWTA  bian-reference: PaymentTransaction.Account (as Payee Account)  general-info: Reference to the account to which the payment is made   # noqa: E501

        :param payment_transaction_payee_account_reference: The payment_transaction_payee_account_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_payee_account_reference: str
        """

        self._payment_transaction_payee_account_reference = payment_transaction_payee_account_reference

    @property
    def payment_transaction_payee_bank_reference(self):
        """Gets the payment_transaction_payee_bank_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EteNyMTGEeChad0JzLk7QA_-246206935  bian-reference: PaymentTransactionInvolvementType (as PayeeBank)  general-info: Reference to the bank where the payee account is held   # noqa: E501

        :return: The payment_transaction_payee_bank_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_payee_bank_reference

    @payment_transaction_payee_bank_reference.setter
    def payment_transaction_payee_bank_reference(self, payment_transaction_payee_bank_reference):
        """Sets the payment_transaction_payee_bank_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_EteNyMTGEeChad0JzLk7QA_-246206935  bian-reference: PaymentTransactionInvolvementType (as PayeeBank)  general-info: Reference to the bank where the payee account is held   # noqa: E501

        :param payment_transaction_payee_bank_reference: The payment_transaction_payee_bank_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_payee_bank_reference: str
        """

        self._payment_transaction_payee_bank_reference = payment_transaction_payee_bank_reference

    @property
    def payment_transaction_amount(self):
        """Gets the payment_transaction_amount of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_xIKY4Hm5EeKIubTif2R3gg_40795932  bian-reference: PaymentTransactionPrincipleAmount  general-info: The amount (and currency if applicable) of the payment   # noqa: E501

        :return: The payment_transaction_amount of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_amount

    @payment_transaction_amount.setter
    def payment_transaction_amount(self, payment_transaction_amount):
        """Sets the payment_transaction_amount of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_xIKY4Hm5EeKIubTif2R3gg_40795932  bian-reference: PaymentTransactionPrincipleAmount  general-info: The amount (and currency if applicable) of the payment   # noqa: E501

        :param payment_transaction_amount: The payment_transaction_amount of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_amount: str
        """

        self._payment_transaction_amount = payment_transaction_amount

    @property
    def payment_transaction_fee_type(self):
        """Gets the payment_transaction_fee_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeTransactionAppliedFeeType  general-info: The fee type applied to the payment transaction   # noqa: E501

        :return: The payment_transaction_fee_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_fee_type

    @payment_transaction_fee_type.setter
    def payment_transaction_fee_type(self, payment_transaction_fee_type):
        """Sets the payment_transaction_fee_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_Fbg_gcTGEeChad0JzLk7QA_-70110816  bian-reference: FeeTransactionAppliedFeeType  general-info: The fee type applied to the payment transaction   # noqa: E501

        :param payment_transaction_fee_type: The payment_transaction_fee_type of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_fee_type: str
        """

        self._payment_transaction_fee_type = payment_transaction_fee_type

    @property
    def payment_transaction_fee_charge(self):
        """Gets the payment_transaction_fee_charge of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_FMBK98TGEeChad0JzLk7QA_-1487452687  bian-reference: FeeTransactionAppliedFeeAmount  general-info: The fee charge applied to the transaction   # noqa: E501

        :return: The payment_transaction_fee_charge of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_fee_charge

    @payment_transaction_fee_charge.setter
    def payment_transaction_fee_charge(self, payment_transaction_fee_charge):
        """Sets the payment_transaction_fee_charge of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_Fbg_gMTGEeChad0JzLk7QA_-330542668/elements/_FMBK98TGEeChad0JzLk7QA_-1487452687  bian-reference: FeeTransactionAppliedFeeAmount  general-info: The fee charge applied to the transaction   # noqa: E501

        :param payment_transaction_fee_charge: The payment_transaction_fee_charge of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_fee_charge: str
        """

        self._payment_transaction_fee_charge = payment_transaction_fee_charge

    @property
    def payment_transaction_date(self):
        """Gets the payment_transaction_date of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FDYMU8TGEeChad0JzLk7QA_1746210992  bian-reference: PaymentTransactionValueDate  general-info: The various key dates and times associated with the payment transaction   # noqa: E501

        :return: The payment_transaction_date of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_date

    @payment_transaction_date.setter
    def payment_transaction_date(self, payment_transaction_date):
        """Sets the payment_transaction_date of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FDYMU8TGEeChad0JzLk7QA_1746210992  bian-reference: PaymentTransactionValueDate  general-info: The various key dates and times associated with the payment transaction   # noqa: E501

        :param payment_transaction_date: The payment_transaction_date of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_date: str
        """

        self._payment_transaction_date = payment_transaction_date

    @property
    def payment_transaction_payment_mechanism(self):
        """Gets the payment_transaction_payment_mechanism of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FAi6ycTGEeChad0JzLk7QA_1746210990  bian-reference: PaymentTransactionUsedMechanism  general-info: Requested payment mechanism (e.g. Wire, ACH)   # noqa: E501

        :return: The payment_transaction_payment_mechanism of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_payment_mechanism

    @payment_transaction_payment_mechanism.setter
    def payment_transaction_payment_mechanism(self, payment_transaction_payment_mechanism):
        """Sets the payment_transaction_payment_mechanism of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FAi6ycTGEeChad0JzLk7QA_1746210990  bian-reference: PaymentTransactionUsedMechanism  general-info: Requested payment mechanism (e.g. Wire, ACH)   # noqa: E501

        :param payment_transaction_payment_mechanism: The payment_transaction_payment_mechanism of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_payment_mechanism: str
        """

        self._payment_transaction_payment_mechanism = payment_transaction_payment_mechanism

    @property
    def payment_transaction_payment_purpose(self):
        """Gets the payment_transaction_payment_purpose of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the purpose including any external reference to the transaction   # noqa: E501

        :return: The payment_transaction_payment_purpose of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_payment_purpose

    @payment_transaction_payment_purpose.setter
    def payment_transaction_payment_purpose(self, payment_transaction_payment_purpose):
        """Sets the payment_transaction_payment_purpose of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Not Mapped`  core-data-type-reference: BIAN::DataTypesLibrary::CoreDataTypes::UNCEFACT::Text  general-info: Description of the purpose including any external reference to the transaction   # noqa: E501

        :param payment_transaction_payment_purpose: The payment_transaction_payment_purpose of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_payment_purpose: str
        """

        self._payment_transaction_payment_purpose = payment_transaction_payment_purpose

    @property
    def payment_transaction_bank_branch_location_reference(self):
        """Gets the payment_transaction_bank_branch_location_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FNqJt8TGEeChad0JzLk7QA_-1317971633/elements/_z2I6YGx5EeKmZJ0Ago--9g_239738909  bian-reference: PaymentTransactionInvolvementAsPartyRole.Party.Location  general-info: Reference to the location the payment transaction is initiated from    # noqa: E501

        :return: The payment_transaction_bank_branch_location_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_bank_branch_location_reference

    @payment_transaction_bank_branch_location_reference.setter
    def payment_transaction_bank_branch_location_reference(self, payment_transaction_bank_branch_location_reference):
        """Sets the payment_transaction_bank_branch_location_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FNqJt8TGEeChad0JzLk7QA_-1317971633/elements/_z2I6YGx5EeKmZJ0Ago--9g_239738909  bian-reference: PaymentTransactionInvolvementAsPartyRole.Party.Location  general-info: Reference to the location the payment transaction is initiated from    # noqa: E501

        :param payment_transaction_bank_branch_location_reference: The payment_transaction_bank_branch_location_reference of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_bank_branch_location_reference: str
        """

        self._payment_transaction_bank_branch_location_reference = payment_transaction_bank_branch_location_reference

    @property
    def payment_transaction_status(self):
        """Gets the payment_transaction_status of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FCe0dcTGEeChad0JzLk7QA_221546661  bian-reference: BankingTransactionStatus  general-info: The processing status of the transaction (e.g. captured, approved, initiated, confirmed, settled)   # noqa: E501

        :return: The payment_transaction_status of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :rtype: str
        """
        return self._payment_transaction_status

    @payment_transaction_status.setter
    def payment_transaction_status(self, payment_transaction_status):
        """Sets the payment_transaction_status of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.

        `status: Registered`  iso-link: https://www.iso20022.org/standardsrepository/public/wqt/Description/mx/dico/bc/_FCL5hcTGEeChad0JzLk7QA_1746210980/elements/_FCe0dcTGEeChad0JzLk7QA_221546661  bian-reference: BankingTransactionStatus  general-info: The processing status of the transaction (e.g. captured, approved, initiated, confirmed, settled)   # noqa: E501

        :param payment_transaction_status: The payment_transaction_status of this BQPaymentsRetrieveOutputModelPaymentsInstanceRecordPaymentTransaction.
        :type payment_transaction_status: str
        """

        self._payment_transaction_status = payment_transaction_status
