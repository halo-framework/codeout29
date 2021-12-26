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
	
from tester.app.dto.inline_object10 import InlineObject10  # noqa: E501
from tester.app.dto.inline_object19 import InlineObject19  # noqa: E501
from tester.app.dto.inline_response20010 import InlineResponse20010  # noqa: E501
from tester.app.dto.inline_response20019 import InlineResponse20019  # noqa: E501
from tester import util

def exchange_current_account_fulfillment_arrangement_account_lien_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Handle an external exchange (e.g. accept, reject, verify)

    Exchange (i.e. confirm, reject) details of an account lien # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountLien Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20010
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

    method_id = "exchange_current_account_fulfillment_arrangement_account_lien_update"

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


def exchange_current_account_fulfillment_arrangement_payments_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Handle an external exchange (e.g. accept, reject, verify)

    Verify/approve a scheduled repeating payment # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: Payments Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20019
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

    method_id = "exchange_current_account_fulfillment_arrangement_payments_update"

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


