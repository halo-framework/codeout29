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
	
from tester.app.dto.inline_object12 import InlineObject12  # noqa: E501
from tester.app.dto.inline_object15 import InlineObject15  # noqa: E501
from tester.app.dto.inline_object18 import InlineObject18  # noqa: E501
from tester.app.dto.inline_object22 import InlineObject22  # noqa: E501
from tester.app.dto.inline_object4 import InlineObject4  # noqa: E501
from tester.app.dto.inline_object9 import InlineObject9  # noqa: E501
from tester.app.dto.inline_response20012 import InlineResponse20012  # noqa: E501
from tester.app.dto.inline_response20015 import InlineResponse20015  # noqa: E501
from tester.app.dto.inline_response20018 import InlineResponse20018  # noqa: E501
from tester.app.dto.inline_response20022 import InlineResponse20022  # noqa: E501
from tester.app.dto.inline_response2003 import InlineResponse2003  # noqa: E501
from tester.app.dto.inline_response2009 import InlineResponse2009  # noqa: E501
from tester import util

def update_current_account_fulfillment_arrangement(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the CurrentAccountFulfillmentArrangement instance

    Update properties of an active current account # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
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

    method_id = "update_current_account_fulfillment_arrangement"

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


def update_current_account_fulfillment_arrangement_account_lien(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the AccountLien instance

    Update details of an existing account lien # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountLien Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2009
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

    method_id = "update_current_account_fulfillment_arrangement_account_lien"

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


def update_current_account_fulfillment_arrangement_account_sweep(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the AccountSweep instance

    Update details of an existing account sweep # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountSweep Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20012
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

    method_id = "update_current_account_fulfillment_arrangement_account_sweep"

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


def update_current_account_fulfillment_arrangement_deposits_and_withdrawals(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the DepositsAndWithdrawals instance

    Update/correct a deposit or withdrawal transaction # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: DepositsAndWithdrawals Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20015
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

    method_id = "update_current_account_fulfillment_arrangement_deposits_and_withdrawals"

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


def update_current_account_fulfillment_arrangement_issued_device(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the IssuedDevice instance

    Update the issued inventory details and provisioning configuration or status # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: IssuedDevice Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20022
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

    method_id = "update_current_account_fulfillment_arrangement_issued_device"

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


def update_current_account_fulfillment_arrangement_payments(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Update to any amendable fields of the Payments instance

    Update a payment transaction configuration or specific transaction # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: Payments Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20018
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

    method_id = "update_current_account_fulfillment_arrangement_payments"

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


