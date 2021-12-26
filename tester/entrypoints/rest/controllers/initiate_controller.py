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
	
from tester.app.dto.inline_object11 import InlineObject11  # noqa: E501
from tester.app.dto.inline_object14 import InlineObject14  # noqa: E501
from tester.app.dto.inline_object17 import InlineObject17  # noqa: E501
from tester.app.dto.inline_object21 import InlineObject21  # noqa: E501
from tester.app.dto.inline_object3 import InlineObject3  # noqa: E501
from tester.app.dto.inline_object6 import InlineObject6  # noqa: E501
from tester.app.dto.inline_object8 import InlineObject8  # noqa: E501
from tester.app.dto.inline_response2011 import InlineResponse2011  # noqa: E501
from tester.app.dto.inline_response2012 import InlineResponse2012  # noqa: E501
from tester.app.dto.inline_response2013 import InlineResponse2013  # noqa: E501
from tester.app.dto.inline_response2014 import InlineResponse2014  # noqa: E501
from tester.app.dto.inline_response2015 import InlineResponse2015  # noqa: E501
from tester.app.dto.inline_response2016 import InlineResponse2016  # noqa: E501
from tester.app.dto.inline_response2017 import InlineResponse2017  # noqa: E501
from tester import util

def initiate_current_account_fulfillment_arrangement(sd_reference_id,body):  # noqa: E501
    """Details of a new CurrentAccountFulfillmentArrangement instance

    Initiate A new Current Account # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2011
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

    method_id = "initiate_current_account_fulfillment_arrangement"

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


def initiate_current_account_fulfillment_arrangement_account_lien(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new AccountLien instance

    Set up an account lien # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2013
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

    method_id = "initiate_current_account_fulfillment_arrangement_account_lien"

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


def initiate_current_account_fulfillment_arrangement_account_sweep(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new AccountSweep instance

    Set up an account sweep # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2014
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

    method_id = "initiate_current_account_fulfillment_arrangement_account_sweep"

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


def initiate_current_account_fulfillment_arrangement_deposits_and_withdrawals(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new DepositsAndWithdrawals instance

    Initialize deposit or withdrawal transaction # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2015
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

    method_id = "initiate_current_account_fulfillment_arrangement_deposits_and_withdrawals"

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


def initiate_current_account_fulfillment_arrangement_issued_device(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new IssuedDevice instance

    Initiate the provision of issued inventory for the account (include initial issuance) # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2017
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

    method_id = "initiate_current_account_fulfillment_arrangement_issued_device"

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


def initiate_current_account_fulfillment_arrangement_payments(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new Payments instance

    Initialize a payment transaction (can be single or repeating) # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2016
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

    method_id = "initiate_current_account_fulfillment_arrangement_payments"

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


def initiate_current_account_fulfillment_arrangement_service_fees(sd_reference_id,cr_reference_id,body):  # noqa: E501
    """Details of a new ServiceFees instance

    Initiate service fees against an account # noqa: E501

    :param sd_reference_id: Current Account Servicing Session Reference
    :type sd_reference_id: str
    :param cr_reference_id: Current Account Fulfillment Arrangement Instance Reference
    :type cr_reference_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2012
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

    method_id = "initiate_current_account_fulfillment_arrangement_service_fees"

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


