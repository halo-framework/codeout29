#!/usr/bin/env python3

import connexion
from typing import Tuple, Dict
from halo_app.app.request import HaloQueryRequest

from tester import util
from halo_app.infra.sql_repository import SqlAlchemyRepository
from halo_app.infra.sql_uow import SqlAlchemyUnitOfWork

from tester.domain.model.model import CurrentAccountFulfillmentArrangement

from tester.domain.model.model import CurrentAccountFulfillmentArrangementAccountLien

from tester.domain.model.model import CurrentAccountFulfillmentArrangementAccountSweep

from tester.domain.model.model import CurrentAccountFulfillmentArrangementDepositsAndWithdrawals

from tester.domain.model.model import CurrentAccountFulfillmentArrangementIssuedDevice

from tester.domain.model.model import CurrentAccountFulfillmentArrangementPayments

from tester.domain.model.model import CurrentAccountFulfillmentArrangementServiceFees


class Repository(SqlAlchemyRepository):
    #@todo fix the name of the aggregate
    def get_type(self) ->type:
        return CurrentAccountFulfillmentArrangement


class Uow(SqlAlchemyUnitOfWork):
    def init_repository(self):
        return Repository(self.session)




