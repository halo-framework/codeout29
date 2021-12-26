#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest


from tester import util

from halo_app.app.context import HaloContext
from halo_app.domain.entity import AbsHaloAggregateRoot, AbsHaloEntity
from halo_app.domain.event import AbsHaloDomainEvent

#@todo fix the type of the aggregate root

class CurrentAccountProps():
    account_number = None
    account_type = None
    customer_id = None
    balance = None

class CurrentAccountFulfillmentArrangement(AbsHaloAggregateRoot,CurrentAccountProps):
    def __init__(self, id: str,props:CurrentAccountProps):
        super(CurrentAccountFulfillmentArrangement, self).__init__(id)
        super(CurrentAccountFulfillmentArrangement, self).__init__(props)
        self.events = []

class AccountLienProps():
    account_number = None
    account_type = None
    customer_id = None
    lien = None

class CurrentAccountFulfillmentArrangementAccountLien(AbsHaloEntity,AccountLienProps):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []


class CurrentAccountFulfillmentArrangementAccountSweep(AbsHaloEntity):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []


class CurrentAccountFulfillmentArrangementDepositsAndWithdrawals(AbsHaloEntity):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []


class CurrentAccountFulfillmentArrangementIssuedDevice(AbsHaloEntity):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []


class CurrentAccountFulfillmentArrangementPayments(AbsHaloEntity):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []


class CurrentAccountFulfillmentArrangementServiceFees(AbsHaloEntity):
    def __init__(self, id: str):
        super().__init__(id)
        self.events = []



