    #!/usr/bin/env python3

import os
import logging
import datetime
import uuid
from halo_app.app.utilx import strx
from halo_app.infra.apis import AbsSoapApi,AbsRestApi
from halo_app.logs import log_json
from halo_app.infra.providers.providers import get_provider

from halo_app.settingsx import settingsx
settings = settingsx()

logger = logging.getLogger(__name__)




