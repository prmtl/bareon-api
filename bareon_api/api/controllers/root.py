# -*- coding: utf-8 -*-

#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import pecan

from bareon_api.api.controllers import actions
from bareon_api.api.controllers import nodes
from bareon_api.common import utils


LOG = utils.getLogger(__name__)


class V1Controller(object):
    """Root controller for the v1 API"""

    def __init__(self):
        LOG.debug('=== Creating V1Controller ===')
        self.nodes = nodes.NodesController()
        self.actions = actions.GlobalActionsController()

    @pecan.expose(generic=True)
    def index(self):
        pecan.abort(405)  # HTTP 405 Method Not Allowed as default
