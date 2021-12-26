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
	
from tester.app.dto.inline_object13 import InlineObject13  # noqa: E501
from tester.app.dto.inline_object16 import InlineObject16  # noqa: E501
from tester.app.dto.inline_object20 import InlineObject20  # noqa: E501
from tester.app.dto.inline_object7 import InlineObject7  # noqa: E501
from tester.app.dto.inline_response20013 import InlineResponse20013  # noqa: E501
from tester.app.dto.inline_response20016 import InlineResponse20016  # noqa: E501
from tester.app.dto.inline_response20020 import InlineResponse20020  # noqa: E501
from tester.app.dto.inline_response2007 import InlineResponse2007  # noqa: E501
from tester import util

def execute_current_account_fulfillment_arrangement_account_sweep_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Invoke an automated execute action against the AccountSweep instance

    Trigger an account sweep transaction # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: AccountSweep Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20013
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

    method_id = "execute_current_account_fulfillment_arrangement_account_sweep_update"

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


def execute_current_account_fulfillment_arrangement_deposits_and_withdrawals_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Invoke an automated execute action against the DepositsAndWithdrawals instance

    Execute a deposit or withdrawal transaction # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: DepositsAndWithdrawals Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20016
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

    method_id = "execute_current_account_fulfillment_arrangement_deposits_and_withdrawals_update"

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


def execute_current_account_fulfillment_arrangement_payments_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Invoke an automated execute action against the Payments instance

    Trigger a payment for a repeating payment set up # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: Payments Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20020
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

    method_id = "execute_current_account_fulfillment_arrangement_payments_update"

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


def execute_current_account_fulfillment_arrangement_service_fees_update(sd_reference_id,cr_reference_id,bq_reference_id,body):  # noqa: E501
    """Invoke an automated execute action against the ServiceFees instance

    Apply a service fee to the account # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param bq_reference_id: ServiceFees Instance Reference
    :type bq_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2007
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

    method_id = "execute_current_account_fulfillment_arrangement_service_fees_update"

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


