#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest

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

from halo_app.app.context import HaloContext

SQL_DICT = {
    "retrieve_current_account" : "select 'current_account_fulfillment_arrangement_retrieve_action_task_reference',1",
    "retrieve_current_account_behavior_qualifier_reference_ids" : "",
    "retrieve_current_account_behavior_qualifiers" : "",
    "retrieve_current_account_fulfillment_arrangement_account_lien" : "Retrieve details about an active account lien .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_account_sweep" : "Retrieve details about an active sweep facility or specific sweep transaction .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_deposits_and_withdrawals" : "Retrieve details about a deposit or withdrawal transaction .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_interest" : "Retrieve details of an interest transaction applied internally to the account .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_issued_device" : "Retrieve details about issued device/inventory .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_payments" : "Retrieve details about a payment transaction or arrangement .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_fulfillment_arrangement_service_fees" : "Retrieve information about a service fee applied to the account .The retrieve operation can have sub qualifiers beyond BQ level, please reffer to the model heriarchy to extend beyond BQ level into APIs retrieving sub-qualifier level information.",
    "retrieve_current_account_reference_ids" : "",
    "retrieve_sd_current_account" : "Analytical views maintained by the SDCurrentAccount service center for management reporting and analysis purposes"
}

