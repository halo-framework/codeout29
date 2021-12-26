#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest
from halo_app.app.uow import AbsUnitOfWork
from halo_bian.bian.app.handler import AbsBianQueryHandler
from halo_bian.bian.bian import ActionTerms
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
from tester.infra.sql.retrieve_sql import SQL_DICT


"""
    # 1. get api definition to access the BANK API  - url + vars dict
    back_api = self.set_back_api(halo_request)
    # 2. array to store the headers required for the API Access
    back_headers = self.set_api_headers(halo_request,back_api)
    # 3. Set request params
    back_vars = self.set_api_vars(halo_request,back_api)
    # 4. Set request auth
    back_auth = self.set_api_auth(halo_request,back_api)
    # 5. Set request data
    if halo_request.request.method == HTTPChoice.post.value or halo_request.request.method == HTTPChoice.put.value:
        back_data = self.set_api_data(halo_request,back_api)
    else:
        back_data = None
    # 6. Sending the request to the BANK API with params
    back_response = self.execute_api(halo_request, back_api, back_vars, back_headers, back_auth,
    back_data)
    # 7. extract from Response stored in an object built as per the BANK API Response body JSON Structure
    back_json = self.extract_json(halo_request,back_api, back_response)
"""


class RetrieveControllerHandler_retrieve_current_account(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params

    def run(self, halo_query_request: HaloQueryRequest,uow:AbsUnitOfWork) -> Dict:
        query_str, dict_params = self.set_query_data(halo_query_request)
        with uow:
            results = list(uow.session.execute(query_str, dict_params))
        return [dict(r) for r in results]



class RetrieveControllerHandler_retrieve_current_account_behavior_qualifier_reference_ids(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_behavior_qualifiers(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_account_lien(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_account_sweep(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_interest(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_issued_device(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_payments(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_fulfillment_arrangement_service_fees(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_current_account_reference_ids(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params



class RetrieveControllerHandler_retrieve_sd_current_account(AbsBianQueryHandler):
    bian_action = ActionTerms.RETRIEVE

    
    def set_query_data(self,halo_query_request: HaloQueryRequest)->Tuple[str,Dict]:
        sql_query = SQL_DICT.get(halo_query_request.usecase_id)
        params = {}
        return sql_query,params




