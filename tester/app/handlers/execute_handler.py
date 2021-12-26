#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest
from halo_bian.bian.app.handler import AbsBianCommandHandler
from halo_bian.bian.bian import ActionTerms
from tester.app.dto.inline_object13 import InlineObject13  # noqa: E501
from tester.app.dto.inline_object16 import InlineObject16  # noqa: E501
from tester.app.dto.inline_object20 import InlineObject20  # noqa: E501
from tester.app.dto.inline_object7 import InlineObject7  # noqa: E501
from tester.app.dto.inline_response20013 import InlineResponse20013  # noqa: E501
from tester.app.dto.inline_response20016 import InlineResponse20016  # noqa: E501
from tester.app.dto.inline_response20020 import InlineResponse20020  # noqa: E501
from tester.app.dto.inline_response2007 import InlineResponse2007  # noqa: E501
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


class ExecuteControllerHandler_execute_current_account_fulfillment_arrangement_account_sweep_update(AbsBianCommandHandler):
    bian_action = ActionTerms.EXECUTE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class ExecuteControllerHandler_execute_current_account_fulfillment_arrangement_deposits_and_withdrawals_update(AbsBianCommandHandler):
    bian_action = ActionTerms.EXECUTE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class ExecuteControllerHandler_execute_current_account_fulfillment_arrangement_payments_update(AbsBianCommandHandler):
    bian_action = ActionTerms.EXECUTE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class ExecuteControllerHandler_execute_current_account_fulfillment_arrangement_service_fees_update(AbsBianCommandHandler):
    bian_action = ActionTerms.EXECUTE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})




