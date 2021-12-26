#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest
from halo_bian.bian.app.handler import AbsBianCommandHandler
from halo_bian.bian.bian import ActionTerms
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


class UpdateControllerHandler_update_current_account_fulfillment_arrangement(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class UpdateControllerHandler_update_current_account_fulfillment_arrangement_account_lien(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class UpdateControllerHandler_update_current_account_fulfillment_arrangement_account_sweep(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class UpdateControllerHandler_update_current_account_fulfillment_arrangement_deposits_and_withdrawals(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class UpdateControllerHandler_update_current_account_fulfillment_arrangement_issued_device(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class UpdateControllerHandler_update_current_account_fulfillment_arrangement_payments(AbsBianCommandHandler):
    bian_action = ActionTerms.UPDATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})




