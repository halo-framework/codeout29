    #!/usr/bin/env python3

import logging
import urllib
import uuid
import requests
import datetime
import json
import traceback
# aws
from botocore.exceptions import ClientError
# halolib
from halo_app.app.viewsx import AbsBaseLinkX as AbsBaseLink
from halo_app.app.utilx import Util, strx
from halo_app.const import HTTPChoice
from halo_app.events import AbsBaseHandler,AbsMainHandler
from halo_app.exceptions import ApiError
from halo_app.logs import log_json
from halo_app.providers.providers import get_provider

from halo_app.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)

class HandlerMixin(AbsMainHandler):
	pass

