#!/usr/bin/env python3


import connexion
import six
from flask import request, jsonify
from halo_app.app.bus import IBus
from halo_app.const import HTTPChoice
from halo_app.sys_util import SysUtil
from halo_bian.bian.util import BianUtil
from halo_bian.bian.app.context import BianContext
from halo_app.entrypoints import client_util
	
from tester.app.dto.inline_response20011 import InlineResponse20011  # noqa: E501
from tester.app.dto.inline_response20014 import InlineResponse20014  # noqa: E501
from tester.app.dto.inline_response20017 import InlineResponse20017  # noqa: E501
from tester.app.dto.inline_response2002 import InlineResponse2002  # noqa: E501
from tester.app.dto.inline_response20021 import InlineResponse20021  # noqa: E501
from tester.app.dto.inline_response20024 import InlineResponse20024  # noqa: E501
from tester.app.dto.inline_response2005 import InlineResponse2005  # noqa: E501
from tester.app.dto.inline_response2006 import InlineResponse2006  # noqa: E501
from tester.app.dto.inline_response2008 import InlineResponse2008  # noqa: E501
from tester import util

def retrieve_current_account(sd_reference_id,cr_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a Current Account Fulfillment Arrangement instance related report

    Retrieve information about a current account - either standard canned reports or selected instance attribute values # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/CRCurrentAccountFulfillmentArrangementRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse2005
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        #payload = api_response.payload
        if api_response.payload:# and isinstance(api_response.payload,list):
            #if len(api_response.payload) == 1:
            #payload = InlineResponse2005.from_dict({"currentAccountFulfillmentArrangementRetrieveActionResponse":"123"})#api_response.payload)
            payload = InlineResponse2005.from_dict(api_response.payload)
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_behavior_qualifier_reference_ids(sd_reference_id,cr_reference_id,behavior_qualifier,collection_filter=None):  # noqa: E501
    """Retrieve Behavior Qualifier Reference Ids

     # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param behavior_qualifier: Behavior Qualifier Name. ex- IssuedDevice
    :type behavior_qualifier: str
    :param collection_filter: Filter to refine the result set. ex- IssuedDevice Instance Status &#x3D; &#39;pending&#39;
    :type collection_filter: str

    :rtype: List[str]
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_behavior_qualifier_reference_ids"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_behavior_qualifiers():  # noqa: E501
    """Retrieve BQ names

     # noqa: E501


    :rtype: List[str]
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_behavior_qualifiers"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_account_lien(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a AccountLien instance related report.

    Retrieve details about an active account lien .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountLien Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQAccountLienRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse20011
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_account_lien"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_account_sweep(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a AccountSweep instance related report.

    Retrieve details about an active sweep facility or specific sweep transaction .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountSweep Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQAccountSweepRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse20014
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_account_sweep"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a DepositsAndWithdrawals instance related report.

    Retrieve details about a deposit or withdrawal transaction .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: DepositsAndWithdrawals Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQDepositsAndWithdrawalsRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse20017
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_interest(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a Interest instance related report.

    Retrieve details of an interest transaction applied internally to the account .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: Interest Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQInterestRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse2006
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_interest"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_issued_device(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a IssuedDevice instance related report.

    Retrieve details about issued device/inventory .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: IssuedDevice Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQIssuedDeviceRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse20024
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_issued_device"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_payments(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a Payments instance related report.

    Retrieve details about a payment transaction or arrangement .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: Payments Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQPaymentsRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse20021
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_payments"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_fulfillment_arrangement_service_fees(sd_reference_id,cr_reference_id,bq_reference_id,queryparams=None):  # noqa: E501
    """Invoke a reporting action to obtain a ServiceFees instance related report.

    Retrieve information about a service fee applied to the account .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information. # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: ServiceFees Instance Reference
    :type bq_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/BQServiceFeesRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse2008
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_fulfillment_arrangement_service_fees"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_current_account_reference_ids(sd_reference_id,collection_filter=None):  # noqa: E501
    """Retrieve CR Ids

     # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param collection_filter: Filter to refine the result set. ex- CurrentAccount Instance Status&#x3D;&#39;active&#39;
    :type collection_filter: str

    :rtype: List[str]
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_current_account_reference_ids"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


def retrieve_sd_current_account(sd_reference_id,queryparams=None):  # noqa: E501
    """Analytical views maintained by the SDCurrentAccount service center for management reporting and analysis purposes

    Analytical views maintained by the SDCurrentAccount service center for management reporting and analysis purposes # noqa: E501

    :param sd_reference_id: SDCurrentAccount Servicing Session Reference
    :type sd_reference_id: str
    :param queryparams: Query params from schema &#39;#/definitions/SDCurrentAccountRetrieveInputModel&#39;
    :type queryparams: str

    :rtype: InlineResponse2002
    """
    try:
        varsx = BianUtil.get_bian_vars(vars())
    except Exception as e:
        error_code = 400
        payload = {"error": {"error_code": error_code, "error_message": e.__str__(),
            "error_detail": 'filter format error',
            "data": e.__cause__,
            "trace_id": request.headers.get(BianContext.CORRELATION)}
            }
        return jsonify(payload), error_code

    bian_context = client_util.get_halo_context(request.headers,request)

    method_id = "retrieve_sd_current_account"

    bus:IBus = SysUtil.get_bus()

    bian_request = BianUtil.create_bian_request(bian_context,method_id,varsx)

    bian_response = bus.execute(bian_request)

    api_response = SysUtil.process_response_for_client(bian_response)

    if api_response.success:
        payload = api_response.payload
    else:
        payload = api_response.error

    headers = BianUtil.get_headers(api_response)

    return jsonify(payload), api_response.code, headers


