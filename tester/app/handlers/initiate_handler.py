#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest
from halo_bian.bian.app.handler import AbsBianCommandHandler
from halo_bian.bian.bian import ActionTerms
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


class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_account_lien(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_account_sweep(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_deposits_and_withdrawals(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_issued_device(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_payments(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})



class InitiateControllerHandler_initiate_current_account_fulfillment_arrangement_service_fees(AbsBianCommandHandler):
    bian_action = ActionTerms.INITIATE

    
    #def handle(self,halo_command_request:HaloCommandRequest,uow:AbsUnitOfWork)->Result:
    #    with uow:
    #         item = uow.repository.get(bian_command_request.cr_reference_id)
    #         entity = self.domain_service.validate(item)
    #         self.infra_service.send(entity)
    #         uow.commit()
    #     return Result.ok({"1":"abc","2":"def"})




