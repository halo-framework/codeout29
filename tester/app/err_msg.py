    #!/usr/bin/env python3

import logging
import urllib
import uuid
import datetime
import json
# common
from halo_app.const import HTTPChoice
from halo_bian.bian.app.err_msg import ErrorMessages





logger = logging.getLogger(__name__)


class ErrorMessages(ErrorMessages):

    #custom messages
    ErrorMessages.hashx["MaxTryException"] = { "code" : 123, "message" : "Server Error" }




